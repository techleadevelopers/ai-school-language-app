
import React, { useState, useEffect } from 'react';
import { View, Text, StyleSheet, TouchableOpacity, Animated } from 'react-native';
import { LinearGradient } from 'expo-linear-gradient';
import { Ionicons } from '@expo/vector-icons';
import { Colors } from '@/constants/Colors';
import { useColorScheme } from '@/hooks/useColorScheme';

interface CoachingTip {
  id: string;
  type: 'pronunciation' | 'grammar' | 'vocabulary' | 'fluency';
  title: string;
  message: string;
  priority: 'low' | 'medium' | 'high';
  action?: string;
}

interface AICoachSystemProps {
  userPerformance: {
    pronunciationScore: number;
    grammarScore: number;
    vocabularyLevel: number;
    fluencyRate: number;
  };
  recentMistakes: string[];
  learningGoals: string[];
}

export function AICoachSystem({ userPerformance, recentMistakes, learningGoals }: AICoachSystemProps) {
  const colorScheme = useColorScheme();
  const colors = Colors[colorScheme ?? 'light'];
  const [coachingTips, setCoachingTips] = useState<CoachingTip[]>([]);
  const [isCoachVisible, setIsCoachVisible] = useState(false);
  const [animatedValue] = useState(new Animated.Value(0));

  useEffect(() => {
    generatePersonalizedTips();
    animateCoachEntry();
  }, [userPerformance, recentMistakes]);

  const animateCoachEntry = () => {
    setIsCoachVisible(true);
    Animated.spring(animatedValue, {
      toValue: 1,
      useNativeDriver: true,
      tension: 100,
      friction: 8,
    }).start();
  };

  const generatePersonalizedTips = () => {
    const tips: CoachingTip[] = [];

    // Análise de pronúncia
    if (userPerformance.pronunciationScore < 70) {
      tips.push({
        id: 'pronunciation-1',
        type: 'pronunciation',
        title: '🎤 Melhore sua Pronúncia',
        message: 'Pratique palavras com sons similares ao português. Foque em "th", "r" e vogais.',
        priority: 'high',
        action: 'Praticar Pronúncia'
      });
    }

    // Análise de gramática
    if (userPerformance.grammarScore < 75) {
      tips.push({
        id: 'grammar-1',
        type: 'grammar',
        title: '📚 Reforce a Gramática',
        message: 'Revise tempos verbais. Identifiquei dificuldades com Present Perfect.',
        priority: 'medium',
        action: 'Exercícios de Gramática'
      });
    }

    // Análise de vocabulário
    if (userPerformance.vocabularyLevel < 60) {
      tips.push({
        id: 'vocabulary-1',
        type: 'vocabulary',
        title: '🧠 Expanda seu Vocabulário',
        message: 'Aprenda 5 palavras novas por dia. Comece com palavras do seu campo profissional.',
        priority: 'medium',
        action: 'Lista de Vocabulário'
      });
    }

    // Análise de fluência
    if (userPerformance.fluencyRate < 65) {
      tips.push({
        id: 'fluency-1',
        type: 'fluency',
        title: '⚡ Desenvolva Fluência',
        message: 'Pratique conversação por 10 minutos diários. Fale sozinho sobre temas variados.',
        priority: 'high',
        action: 'Prática de Conversação'
      });
    }

    // Dicas baseadas em erros recentes
    if (recentMistakes.length > 0) {
      tips.push({
        id: 'mistakes-1',
        type: 'grammar',
        title: '🔍 Corrija Erros Frequentes',
        message: `Você cometeu ${recentMistakes.length} erros similares recentemente. Vamos focar nisso!`,
        priority: 'high',
        action: 'Revisar Erros'
      });
    }

    setCoachingTips(tips.slice(0, 3)); // Máximo 3 dicas por vez
  };

  const getPriorityColor = (priority: string) => {
    switch (priority) {
      case 'high': return '#F44336';
      case 'medium': return '#FF9800';
      case 'low': return '#4CAF50';
      default: return colors.text;
    }
  };

  const getTypeIcon = (type: string) => {
    switch (type) {
      case 'pronunciation': return 'mic';
      case 'grammar': return 'library';
      case 'vocabulary': return 'book';
      case 'fluency': return 'chatbubbles';
      default: return 'bulb';
    }
  };

  const handleTipAction = (tip: CoachingTip) => {
    // Implementar navegação para ação específica
    console.log(`Executing action: ${tip.action} for tip: ${tip.id}`);
  };

  const dismissTip = (tipId: string) => {
    setCoachingTips(tips => tips.filter(tip => tip.id !== tipId));
  };

  if (!isCoachVisible || coachingTips.length === 0) {
    return null;
  }

  return (
    <Animated.View 
      style={[
        styles.container, 
        { 
          backgroundColor: colors.background,
          transform: [
            {
              translateY: animatedValue.interpolate({
                inputRange: [0, 1],
                outputRange: [100, 0],
              }),
            },
            {
              scale: animatedValue.interpolate({
                inputRange: [0, 1],
                outputRange: [0.8, 1],
              }),
            },
          ],
        }
      ]}
    >
      <LinearGradient
        colors={['#667eea', '#764ba2']}
        style={styles.header}
      >
        <View style={styles.coachHeader}>
          <View style={styles.avatarContainer}>
            <Text style={styles.avatarEmoji}>🤖</Text>
          </View>
          <View style={styles.coachInfo}>
            <Text style={styles.coachName}>AI Coach</Text>
            <Text style={styles.coachStatus}>Analisando seu progresso...</Text>
          </View>
          <TouchableOpacity 
            style={styles.closeButton}
            onPress={() => setIsCoachVisible(false)}
          >
            <Ionicons name="close" size={20} color="white" />
          </TouchableOpacity>
        </View>
      </LinearGradient>

      <View style={styles.tipsContainer}>
        {coachingTips.map((tip, index) => (
          <View key={tip.id} style={[styles.tipCard, { backgroundColor: colors.background }]}>
            <View style={styles.tipHeader}>
              <View style={styles.tipIconContainer}>
                <Ionicons 
                  name={getTypeIcon(tip.type) as any} 
                  size={20} 
                  color={getPriorityColor(tip.priority)} 
                />
              </View>
              <View style={styles.tipContent}>
                <Text style={[styles.tipTitle, { color: colors.text }]}>{tip.title}</Text>
                <Text style={[styles.tipMessage, { color: colors.text + 'CC' }]}>
                  {tip.message}
                </Text>
              </View>
              <View style={[styles.priorityIndicator, { backgroundColor: getPriorityColor(tip.priority) }]} />
            </View>

            <View style={styles.tipActions}>
              {tip.action && (
                <TouchableOpacity
                  style={[styles.actionButton, { backgroundColor: getPriorityColor(tip.priority) }]}
                  onPress={() => handleTipAction(tip)}
                >
                  <Text style={styles.actionButtonText}>{tip.action}</Text>
                </TouchableOpacity>
              )}
              
              <TouchableOpacity
                style={[styles.dismissButton, { borderColor: colors.text + '30' }]}
                onPress={() => dismissTip(tip.id)}
              >
                <Text style={[styles.dismissButtonText, { color: colors.text + 'CC' }]}>
                  Dispensar
                </Text>
              </TouchableOpacity>
            </View>
          </View>
        ))}
      </View>

      <View style={styles.motivationalSection}>
        <Text style={[styles.motivationalText, { color: colors.text }]}>
          💪 Continue assim! Você está no caminho certo para dominar o inglês!
        </Text>
      </View>
    </Animated.View>
  );
}

const styles = StyleSheet.create({
  container: {
    margin: 16,
    borderRadius: 16,
    overflow: 'hidden',
    elevation: 8,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 4 },
    shadowOpacity: 0.2,
    shadowRadius: 8,
  },
  header: {
    padding: 16,
  },
  coachHeader: {
    flexDirection: 'row',
    alignItems: 'center',
  },
  avatarContainer: {
    width: 48,
    height: 48,
    borderRadius: 24,
    backgroundColor: 'rgba(255,255,255,0.2)',
    justifyContent: 'center',
    alignItems: 'center',
  },
  avatarEmoji: {
    fontSize: 24,
  },
  coachInfo: {
    flex: 1,
    marginLeft: 12,
  },
  coachName: {
    color: 'white',
    fontSize: 18,
    fontWeight: 'bold',
  },
  coachStatus: {
    color: 'rgba(255,255,255,0.8)',
    fontSize: 14,
  },
  closeButton: {
    width: 32,
    height: 32,
    borderRadius: 16,
    backgroundColor: 'rgba(255,255,255,0.2)',
    justifyContent: 'center',
    alignItems: 'center',
  },
  tipsContainer: {
    padding: 16,
  },
  tipCard: {
    marginBottom: 16,
    padding: 16,
    borderRadius: 12,
    borderWidth: 1,
    borderColor: 'rgba(0,0,0,0.1)',
  },
  tipHeader: {
    flexDirection: 'row',
    alignItems: 'flex-start',
    marginBottom: 12,
  },
  tipIconContainer: {
    width: 40,
    height: 40,
    borderRadius: 20,
    backgroundColor: 'rgba(0,0,0,0.05)',
    justifyContent: 'center',
    alignItems: 'center',
    marginRight: 12,
  },
  tipContent: {
    flex: 1,
  },
  tipTitle: {
    fontSize: 16,
    fontWeight: 'bold',
    marginBottom: 4,
  },
  tipMessage: {
    fontSize: 14,
    lineHeight: 20,
  },
  priorityIndicator: {
    width: 8,
    height: 8,
    borderRadius: 4,
    marginLeft: 8,
    marginTop: 4,
  },
  tipActions: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
  },
  actionButton: {
    paddingHorizontal: 16,
    paddingVertical: 8,
    borderRadius: 20,
    flex: 1,
    marginRight: 8,
  },
  actionButtonText: {
    color: 'white',
    fontWeight: 'bold',
    textAlign: 'center',
  },
  dismissButton: {
    paddingHorizontal: 16,
    paddingVertical: 8,
    borderRadius: 20,
    borderWidth: 1,
  },
  dismissButtonText: {
    fontWeight: '500',
  },
  motivationalSection: {
    padding: 16,
    borderTopWidth: 1,
    borderTopColor: 'rgba(0,0,0,0.1)',
  },
  motivationalText: {
    fontSize: 16,
    fontWeight: '500',
    textAlign: 'center',
    lineHeight: 24,
  },
});
