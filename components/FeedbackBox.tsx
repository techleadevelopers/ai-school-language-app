
import React from 'react';
import { View, StyleSheet, Animated } from 'react-native';
import { useThemeColor } from '@/hooks/useThemeColor';
import Typography from './Typography';
import { Ionicons } from '@expo/vector-icons';

interface FeedbackData {
  transcription: string;
  score: number;
  feedback: string;
  suggestions: string[];
  correctPhrase: string;
  accuracy: number;
  pronunciationScore?: number;
  fluencyScore?: number;
  grammarScore?: number;
  aiInsights?: string[];
}

interface FeedbackBoxProps {
  feedback: FeedbackData | null;
  isVisible: boolean;
}

export const FeedbackBox = ({ feedback, isVisible }: FeedbackBoxProps) => {
  const backgroundColor = useThemeColor({}, 'background');
  const borderColor = useThemeColor({}, 'tint');
  const textColor = useThemeColor({}, 'text');
  
  const fadeAnim = React.useRef(new Animated.Value(0)).current;

  React.useEffect(() => {
    if (isVisible && feedback) {
      Animated.timing(fadeAnim, {
        toValue: 1,
        duration: 500,
        useNativeDriver: true,
      }).start();
    } else {
      fadeAnim.setValue(0);
    }
  }, [isVisible, feedback]);

  if (!feedback || !isVisible) return null;

  const getScoreColor = (score: number) => {
    if (score >= 90) return '#4CAF50';
    if (score >= 70) return '#FF9800';
    return '#F44336';
  };

  const getGrade = (score: number) => {
    if (score >= 95) return 'Perfeito! 🎉';
    if (score >= 85) return 'Excelente! 🌟';
    if (score >= 70) return 'Bom trabalho! 👍';
    return 'Continue praticando! 💪';
  };

  return (
    <Animated.View style={[
      styles.container,
      { backgroundColor, borderColor, opacity: fadeAnim }
    ]}>
      {/* Score Header */}
      <View style={styles.scoreHeader}>
        <View style={[styles.scoreCircle, { borderColor: getScoreColor(feedback.score) }]}>
          <Typography type="title" style={{ color: getScoreColor(feedback.score) }}>
            {feedback.score}
          </Typography>
        </View>
        <View style={styles.gradeContainer}>
          <Typography type="subtitle">{getGrade(feedback.score)}</Typography>
          <Typography type="default" style={styles.accuracyText}>
            Precisão: {feedback.accuracy}%
          </Typography>
        </View>
      </View>

      {/* Transcription Comparison */}
      <View style={styles.section}>
        <Typography type="subtitle" style={styles.sectionTitle}>
          <Ionicons name="text" size={16} /> Transcrição
        </Typography>
        <View style={styles.transcriptionContainer}>
          <Typography type="default" style={styles.originalText}>
            Original: "{feedback.correctPhrase}"
          </Typography>
          <Typography type="default" style={styles.transcribedText}>
            Você disse: "{feedback.transcription}"
          </Typography>
        </View>
      </View>

      {/* Detailed Scores */}
      {(feedback.pronunciationScore || feedback.fluencyScore || feedback.grammarScore) && (
        <View style={styles.section}>
          <Typography type="subtitle" style={styles.sectionTitle}>
            <Ionicons name="analytics" size={16} /> Análise Detalhada
          </Typography>
          <View style={styles.scoresGrid}>
            {feedback.pronunciationScore && (
              <View style={styles.scoreItem}>
                <Typography type="default">Pronúncia</Typography>
                <Typography type="subtitle" style={{ color: getScoreColor(feedback.pronunciationScore) }}>
                  {feedback.pronunciationScore}%
                </Typography>
              </View>
            )}
            {feedback.fluencyScore && (
              <View style={styles.scoreItem}>
                <Typography type="default">Fluência</Typography>
                <Typography type="subtitle" style={{ color: getScoreColor(feedback.fluencyScore) }}>
                  {feedback.fluencyScore}%
                </Typography>
              </View>
            )}
            {feedback.grammarScore && (
              <View style={styles.scoreItem}>
                <Typography type="default">Gramática</Typography>
                <Typography type="subtitle" style={{ color: getScoreColor(feedback.grammarScore) }}>
                  {feedback.grammarScore}%
                </Typography>
              </View>
            )}
          </View>
        </View>
      )}

      {/* AI Feedback */}
      <View style={styles.section}>
        <Typography type="subtitle" style={styles.sectionTitle}>
          <Ionicons name="bulb" size={16} /> Feedback da IA
        </Typography>
        <Typography type="default" style={styles.feedbackText}>
          {feedback.feedback}
        </Typography>
      </View>

      {/* Suggestions */}
      {feedback.suggestions && feedback.suggestions.length > 0 && (
        <View style={styles.section}>
          <Typography type="subtitle" style={styles.sectionTitle}>
            <Ionicons name="checkmark-circle" size={16} /> Sugestões
          </Typography>
          {feedback.suggestions.map((suggestion, index) => (
            <View key={index} style={styles.suggestionItem}>
              <Typography type="default">• {suggestion}</Typography>
            </View>
          ))}
        </View>
      )}

      {/* AI Insights */}
      {feedback.aiInsights && feedback.aiInsights.length > 0 && (
        <View style={styles.section}>
          <Typography type="subtitle" style={styles.sectionTitle}>
            <Ionicons name="brain" size={16} /> Insights da IA
          </Typography>
          {feedback.aiInsights.map((insight, index) => (
            <View key={index} style={styles.insightItem}>
              <Typography type="default" style={styles.insightText}>
                💡 {insight}
              </Typography>
            </View>
          ))}
        </View>
      )}
    </Animated.View>
  );
};

const styles = StyleSheet.create({
  container: {
    margin: 16,
    padding: 20,
    borderRadius: 16,
    borderWidth: 2,
    elevation: 8,
    shadowOffset: { width: 0, height: 4 },
    shadowOpacity: 0.15,
    shadowRadius: 8,
    shadowColor: '#000',
  },
  scoreHeader: {
    flexDirection: 'row',
    alignItems: 'center',
    marginBottom: 20,
  },
  scoreCircle: {
    width: 80,
    height: 80,
    borderRadius: 40,
    borderWidth: 3,
    justifyContent: 'center',
    alignItems: 'center',
    marginRight: 16,
  },
  gradeContainer: {
    flex: 1,
  },
  accuracyText: {
    opacity: 0.7,
    marginTop: 4,
  },
  section: {
    marginBottom: 16,
  },
  sectionTitle: {
    marginBottom: 8,
    opacity: 0.8,
  },
  transcriptionContainer: {
    backgroundColor: 'rgba(0,0,0,0.05)',
    padding: 12,
    borderRadius: 8,
  },
  originalText: {
    fontStyle: 'italic',
    marginBottom: 4,
  },
  transcribedText: {
    fontWeight: '600',
  },
  scoresGrid: {
    flexDirection: 'row',
    justifyContent: 'space-around',
  },
  scoreItem: {
    alignItems: 'center',
  },
  feedbackText: {
    lineHeight: 20,
  },
  suggestionItem: {
    marginBottom: 4,
  },
  insightItem: {
    backgroundColor: 'rgba(66, 165, 245, 0.1)',
    padding: 8,
    borderRadius: 6,
    marginBottom: 4,
  },
  insightText: {
    fontSize: 14,
  },
});
