
from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
from datetime import datetime, timedelta
import io
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from typing import Dict, List, Any
import numpy as np
import base64

class PDFReportService:
    """
    Advanced PDF report generation service for Bilingui-AI
    Generates comprehensive weekly/monthly progress reports
    """
    
    def __init__(self):
        self.styles = getSampleStyleSheet()
        self.setup_custom_styles()
    
    def setup_custom_styles(self):
        """Setup custom styles for the PDF report"""
        self.title_style = ParagraphStyle(
            'CustomTitle',
            parent=self.styles['Heading1'],
            fontSize=24,
            spaceAfter=30,
            alignment=TA_CENTER,
            textColor=colors.HexColor('#2E3B4E')
        )
        
        self.subtitle_style = ParagraphStyle(
            'CustomSubtitle',
            parent=self.styles['Heading2'],
            fontSize=16,
            spaceAfter=20,
            textColor=colors.HexColor('#4A90E2')
        )
        
        self.metric_style = ParagraphStyle(
            'MetricStyle',
            parent=self.styles['Normal'],
            fontSize=12,
            spaceAfter=10,
            leftIndent=20
        )
    
    async def generate_weekly_report(self, user_id: str, user_data: Dict[str, Any]) -> bytes:
        """
        Generate comprehensive weekly progress report
        """
        buffer = io.BytesIO()
        doc = SimpleDocTemplate(
            buffer,
            pagesize=A4,
            rightMargin=72,
            leftMargin=72,
            topMargin=72,
            bottomMargin=18
        )
        
        # Build story (content)
        story = []
        
        # Header
        story.append(Paragraph("📊 RELATÓRIO SEMANAL DE PROGRESSO", self.title_style))
        story.append(Paragraph(f"Bilingui-AI • {datetime.now().strftime('%d/%m/%Y')}", self.styles['Normal']))
        story.append(Spacer(1, 30))
        
        # User Info Section
        story.extend(self._build_user_info_section(user_data))
        story.append(Spacer(1, 20))
        
        # Performance Overview
        story.extend(self._build_performance_overview(user_data))
        story.append(Spacer(1, 20))
        
        # Learning Statistics
        story.extend(self._build_learning_statistics(user_data))
        story.append(Spacer(1, 20))
        
        # Skills Analysis
        story.extend(self._build_skills_analysis(user_data))
        story.append(Spacer(1, 20))
        
        # AI Insights
        story.extend(self._build_ai_insights(user_data))
        story.append(Spacer(1, 20))
        
        # Goals and Recommendations
        story.extend(self._build_recommendations(user_data))
        
        # Build PDF
        doc.build(story)
        buffer.seek(0)
        return buffer.getvalue()
    
    def _build_user_info_section(self, user_data: Dict[str, Any]) -> List:
        """Build user information section"""
        elements = []
        
        elements.append(Paragraph("👤 INFORMAÇÕES DO USUÁRIO", self.subtitle_style))
        
        user_info_data = [
            ['Nome:', user_data.get('name', 'N/A')],
            ['Email:', user_data.get('email', 'N/A')],
            ['Nível Atual:', f"Level {user_data.get('level', 0)}"],
            ['XP Total:', f"{user_data.get('total_xp', 0):,} pontos"],
            ['Sequência Atual:', f"{user_data.get('streak', 0)} dias"],
            ['Data de Início:', user_data.get('start_date', 'N/A')],
        ]
        
        user_table = Table(user_info_data, colWidths=[2*inch, 3*inch])
        user_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (0, -1), colors.HexColor('#F8F9FA')),
            ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 10),
            ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#E0E0E0')),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ]))
        
        elements.append(user_table)
        return elements
    
    def _build_performance_overview(self, user_data: Dict[str, Any]) -> List:
        """Build performance overview section"""
        elements = []
        
        elements.append(Paragraph("📈 RESUMO DE PERFORMANCE", self.subtitle_style))
        
        # Performance metrics
        performance_data = [
            ['Métrica', 'Esta Semana', 'Semana Anterior', 'Variação'],
            ['Lições Completadas', str(user_data.get('lessons_completed', 0)), 
             str(user_data.get('prev_lessons_completed', 0)), 
             self._calculate_change(user_data.get('lessons_completed', 0), 
                                  user_data.get('prev_lessons_completed', 0))],
            ['Tempo de Estudo', f"{user_data.get('study_time', 0)} min", 
             f"{user_data.get('prev_study_time', 0)} min",
             self._calculate_change(user_data.get('study_time', 0), 
                                  user_data.get('prev_study_time', 0))],
            ['Pontuação Média', f"{user_data.get('avg_score', 0):.1f}%", 
             f"{user_data.get('prev_avg_score', 0):.1f}%",
             self._calculate_change(user_data.get('avg_score', 0), 
                                  user_data.get('prev_avg_score', 0))],
            ['XP Ganho', str(user_data.get('xp_gained', 0)), 
             str(user_data.get('prev_xp_gained', 0)),
             self._calculate_change(user_data.get('xp_gained', 0), 
                                  user_data.get('prev_xp_gained', 0))],
        ]
        
        performance_table = Table(performance_data, colWidths=[2*inch, 1.2*inch, 1.2*inch, 1*inch])
        performance_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#4A90E2')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 9),
            ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#E0E0E0')),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#F8F9FA')]),
        ]))
        
        elements.append(performance_table)
        return elements
    
    def _build_learning_statistics(self, user_data: Dict[str, Any]) -> List:
        """Build learning statistics section"""
        elements = []
        
        elements.append(Paragraph("📚 ESTATÍSTICAS DE APRENDIZADO", self.subtitle_style))
        
        # Create chart for learning progress
        chart_buffer = self._create_progress_chart(user_data)
        if chart_buffer:
            # Convert chart to image and add to PDF
            chart_img = Image(chart_buffer, width=5*inch, height=3*inch)
            elements.append(chart_img)
        
        # Learning breakdown
        learning_data = [
            ['Categoria', 'Tempo Gasto', 'Precisão', 'Progresso'],
            ['🗣️ Pronúncia', f"{user_data.get('pronunciation_time', 0)} min", 
             f"{user_data.get('pronunciation_accuracy', 0):.1f}%", 
             f"{user_data.get('pronunciation_progress', 0):.1f}%"],
            ['📖 Vocabulário', f"{user_data.get('vocabulary_time', 0)} min", 
             f"{user_data.get('vocabulary_accuracy', 0):.1f}%", 
             f"{user_data.get('vocabulary_progress', 0):.1f}%"],
            ['📝 Gramática', f"{user_data.get('grammar_time', 0)} min", 
             f"{user_data.get('grammar_accuracy', 0):.1f}%", 
             f"{user_data.get('grammar_progress', 0):.1f}%"],
            ['💬 Conversação', f"{user_data.get('conversation_time', 0)} min", 
             f"{user_data.get('conversation_accuracy', 0):.1f}%", 
             f"{user_data.get('conversation_progress', 0):.1f}%"],
        ]
        
        learning_table = Table(learning_data, colWidths=[1.5*inch, 1.2*inch, 1.2*inch, 1.2*inch])
        learning_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#28A745')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 9),
            ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#E0E0E0')),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#F8F9FA')]),
        ]))
        
        elements.append(Spacer(1, 10))
        elements.append(learning_table)
        return elements
    
    def _build_skills_analysis(self, user_data: Dict[str, Any]) -> List:
        """Build skills analysis section"""
        elements = []
        
        elements.append(Paragraph("🎯 ANÁLISE DE HABILIDADES", self.subtitle_style))
        
        # Skills radar chart would go here
        elements.append(Paragraph("Pontos Fortes:", self.metric_style))
        strengths = user_data.get('strengths', ['Vocabulário', 'Compreensão auditiva'])
        for strength in strengths:
            elements.append(Paragraph(f"• {strength}", self.styles['Normal']))
        
        elements.append(Spacer(1, 10))
        elements.append(Paragraph("Áreas para Melhoria:", self.metric_style))
        weaknesses = user_data.get('weaknesses', ['Pronúncia', 'Gramática avançada'])
        for weakness in weaknesses:
            elements.append(Paragraph(f"• {weakness}", self.styles['Normal']))
        
        return elements
    
    def _build_ai_insights(self, user_data: Dict[str, Any]) -> List:
        """Build AI insights section"""
        elements = []
        
        elements.append(Paragraph("🤖 INSIGHTS DA IA", self.subtitle_style))
        
        insights = user_data.get('ai_insights', [
            "Você demonstra excelente progresso em vocabulário básico.",
            "Recomenda-se mais prática em pronúncia de sons específicos.",
            "Seu padrão de estudo é consistente - continue assim!",
            "Considere aumentar a prática de conversação para melhorar a fluência."
        ])
        
        for insight in insights:
            elements.append(Paragraph(f"• {insight}", self.styles['Normal']))
            elements.append(Spacer(1, 5))
        
        return elements
    
    def _build_recommendations(self, user_data: Dict[str, Any]) -> List:
        """Build recommendations section"""
        elements = []
        
        elements.append(Paragraph("🎖️ METAS E RECOMENDAÇÕES", self.subtitle_style))
        
        # Weekly goals
        elements.append(Paragraph("Metas para a Próxima Semana:", self.metric_style))
        goals = user_data.get('weekly_goals', [
            "Completar 5 lições de pronúncia",
            "Manter sequência de estudos por 7 dias",
            "Alcançar 85% de precisão em exercícios",
            "Praticar conversação por 30 minutos"
        ])
        
        for goal in goals:
            elements.append(Paragraph(f"□ {goal}", self.styles['Normal']))
            elements.append(Spacer(1, 3))
        
        elements.append(Spacer(1, 15))
        
        # Personalized recommendations
        elements.append(Paragraph("Recomendações Personalizadas:", self.metric_style))
        recommendations = user_data.get('recommendations', [
            "Foque em exercícios de listening com sotaque americano",
            "Use a ferramenta de chat com IA para praticar conversação",
            "Revise irregulares verbos 2-3 vezes por semana",
            "Participe dos desafios multiplayer para maior motivação"
        ])
        
        for rec in recommendations:
            elements.append(Paragraph(f"💡 {rec}", self.styles['Normal']))
            elements.append(Spacer(1, 3))
        
        # Footer motivation
        elements.append(Spacer(1, 30))
        elements.append(Paragraph(
            "🌟 Continue seu excelente trabalho! O aprendizado de idiomas é uma jornada, "
            "e você está fazendo progressos notáveis. Lembre-se: consistência é a chave do sucesso!",
            self.styles['Italic']
        ))
        
        return elements
    
    def _create_progress_chart(self, user_data: Dict[str, Any]) -> io.BytesIO:
        """Create progress chart for the last 7 days"""
        try:
            # Generate sample data for the last 7 days
            dates = [datetime.now() - timedelta(days=i) for i in range(6, -1, -1)]
            xp_values = user_data.get('daily_xp', [50, 75, 120, 90, 110, 80, 140])
            
            plt.figure(figsize=(8, 4))
            plt.plot(dates, xp_values, marker='o', linewidth=2, markersize=6, color='#4A90E2')
            plt.fill_between(dates, xp_values, alpha=0.3, color='#4A90E2')
            
            plt.title('Progresso Diário (XP Ganho)', fontsize=14, fontweight='bold')
            plt.xlabel('Data', fontsize=10)
            plt.ylabel('XP Ganho', fontsize=10)
            plt.xticks(rotation=45)
            plt.grid(True, alpha=0.3)
            plt.tight_layout()
            
            # Save chart to buffer
            buffer = io.BytesIO()
            plt.savefig(buffer, format='png', dpi=150, bbox_inches='tight')
            plt.close()
            buffer.seek(0)
            return buffer
            
        except Exception as e:
            print(f"Error creating chart: {e}")
            return None
    
    def _calculate_change(self, current: float, previous: float) -> str:
        """Calculate percentage change between two values"""
        if previous == 0:
            return "N/A"
        
        change = ((current - previous) / previous) * 100
        if change > 0:
            return f"+{change:.1f}%"
        elif change < 0:
            return f"{change:.1f}%"
        else:
            return "0%"

# Initialize service
pdf_report_service = PDFReportService()
