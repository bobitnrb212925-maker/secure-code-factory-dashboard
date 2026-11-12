
from django.shortcuts import render
from django.db.models import Count
from .models import SecurityFinding, SITFPillar
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import io
import base64


def make_chart(labels, values, title, xlabel, ylabel):
    plt.figure(figsize=(7, 4))
    plt.bar(labels, values)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=20, ha='right')
    plt.tight_layout()

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png', bbox_inches='tight')
    buffer.seek(0)

    chart = base64.b64encode(buffer.getvalue()).decode()
    plt.close()

    return chart


def dashboard_home(request):
    findings = SecurityFinding.objects.select_related('pillar').all()

    # Overall statistics
    total = findings.count()
    open_findings = findings.filter(status='Open').count()
    resolved = findings.filter(status='Resolved').count()
    critical = findings.filter(severity='Critical').count()

    # Filters
    selected_severity = request.GET.get('severity', '')
    selected_pillar = request.GET.get('pillar', '')

    filtered_findings = findings

    if selected_severity:
        filtered_findings = filtered_findings.filter(
            severity=selected_severity
        )

    if selected_pillar:
        filtered_findings = filtered_findings.filter(
            pillar_id=selected_pillar
        )

    # Chart data
    severity_data = findings.values('severity').annotate(
        count=Count('id')
    )

    pillar_data = findings.values('pillar__name').annotate(
        count=Count('id')
    )

    severity_chart = make_chart(
        [item['severity'] for item in severity_data],
        [item['count'] for item in severity_data],
        'Findings by Severity',
        'Severity',
        'Number of Findings'
    )

    pillar_chart = make_chart(
        [item['pillar__name'] for item in pillar_data],
        [item['count'] for item in pillar_data],
        'Findings by SITF Pillar',
        'SITF Pillar',
        'Number of Findings'
    )

    context = {
        'total': total,
        'open_findings': open_findings,
        'resolved': resolved,
        'critical': critical,
        'severity_chart': severity_chart,
        'pillar_chart': pillar_chart,
        'findings': filtered_findings.order_by('-created_at'),
        'pillars': SITFPillar.objects.all(),
        'selected_severity': selected_severity,
        'selected_pillar': selected_pillar,
    }

    return render(request, 'dashboard/home.html', context)
