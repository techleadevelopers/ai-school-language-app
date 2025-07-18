
import React, { useState } from 'react';
import { View, Text, StyleSheet, TouchableOpacity, Dimensions } from 'react-native';
import { Ionicons } from '@expo/vector-icons';
import { useRouter } from 'expo-router';
import Typography from '@/components/Typography';
import PrimaryButton from '@/components/PrimaryButton';
import { useThemeColor } from '@/hooks/useThemeColor';

const { width, height } = Dimensions.get('window');

interface OnboardingStep {
  id: number;
  title: string;
  description: string;
  icon: keyof typeof Ionicons.glyphMap;
  color: string;
}

const onboardingSteps: OnboardingStep[] = [
  {
    id: 1,
    title: 'Fale e Aprenda',
    description: 'Use sua voz para praticar pronúncia com feedback em tempo real da nossa IA',
    icon: 'mic',
    color: '#4A90E2'
  },
  {
    id: 2,
    title: 'Chat Inteligente',
    description: 'Converse com nossa IA contextual que se adapta ao seu nível de aprendizado',
    icon: 'chatbubbles',
    color: '#50C878'
  },
  {
    id: 3,
    title: 'Progresso Gamificado',
    description: 'Ganhe XP, desbloqueie conquistas e mantenha sua sequência de estudos',
    icon: 'trophy',
    color: '#FFD700'
  },
  {
    id: 4,
    title: 'Lições Adaptativas',
    description: 'Aprenda no seu ritmo com lições que se ajustam ao seu progresso',
    icon: 'school',
    color: '#FF6B35'
  }
];

export default function OnboardingScreen() {
  const [currentStep, setCurrentStep] = useState(0);
  const [userProfile, setUserProfile] = useState({
    name: '',
    nativeLanguage: '',
    targetLanguage: '',
    experienceLevel: '',
    dailyGoal: 15
  });

  const router = useRouter();
  const backgroundColor = useThemeColor({}, 'background');
  const textColor = useThemeColor({}, 'text');
  const tintColor = useThemeColor({}, 'tint');

  const currentStepData = onboardingSteps[currentStep];

  const handleNext = () => {
    if (currentStep < onboardingSteps.length - 1) {
      setCurrentStep(currentStep + 1);
    } else {
      // Complete onboarding
      completeOnboarding();
    }
  };

  const handleSkip = () => {
    router.replace('/(tabs)');
  };

  const completeOnboarding = async () => {
    // Save user profile and preferences
    try {
      // Here you would save to AsyncStorage and/or send to backend
      console.log('Saving user profile:', userProfile);
      router.replace('/(tabs)');
    } catch (error) {
      console.error('Error saving onboarding data:', error);
    }
  };

  return (
    <View style={[styles.container, { backgroundColor }]}>
      {/* Progress Indicator */}
      <View style={styles.progressContainer}>
        {onboardingSteps.map((_, index) => (
          <View
            key={index}
            style={[
              styles.progressDot,
              {
                backgroundColor: index <= currentStep ? tintColor : '#E0E0E0',
              }
            ]}
          />
        ))}
      </View>

      {/* Skip Button */}
      <TouchableOpacity style={styles.skipButton} onPress={handleSkip}>
        <Text style={[styles.skipText, { color: textColor }]}>Pular</Text>
      </TouchableOpacity>

      {/* Main Content */}
      <View style={styles.contentContainer}>
        <View style={[styles.iconContainer, { backgroundColor: currentStepData.color + '20' }]}>
          <Ionicons 
            name={currentStepData.icon} 
            size={80} 
            color={currentStepData.color} 
          />
        </View>

        <Typography type="headline" style={[styles.title, { color: textColor }]}>
          {currentStepData.title}
        </Typography>

        <Typography style={[styles.description, { color: textColor }]}>
          {currentStepData.description}
        </Typography>

        {/* Interactive Elements for Profile Setup */}
        {currentStep === 0 && (
          <View style={styles.profileSetup}>
            <Typography style={styles.inputLabel}>Qual é o seu nome?</Typography>
            {/* Add TextInput here */}
          </View>
        )}

        {currentStep === 1 && (
          <View style={styles.profileSetup}>
            <Typography style={styles.inputLabel}>Qual idioma você quer aprender?</Typography>
            {/* Add language selection here */}
          </View>
        )}

        {currentStep === 2 && (
          <View style={styles.profileSetup}>
            <Typography style={styles.inputLabel}>Qual é o seu nível?</Typography>
            {/* Add level selection here */}
          </View>
        )}
      </View>

      {/* Navigation Buttons */}
      <View style={styles.navigationContainer}>
        {currentStep > 0 && (
          <TouchableOpacity 
            style={styles.backButton} 
            onPress={() => setCurrentStep(currentStep - 1)}
          >
            <Ionicons name="chevron-back" size={24} color={tintColor} />
            <Text style={[styles.backText, { color: tintColor }]}>Voltar</Text>
          </TouchableOpacity>
        )}

        <PrimaryButton
          title={currentStep === onboardingSteps.length - 1 ? 'Começar' : 'Próximo'}
          onPress={handleNext}
          style={styles.nextButton}
        />
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    paddingHorizontal: 24,
    paddingTop: 60,
  },
  progressContainer: {
    flexDirection: 'row',
    justifyContent: 'center',
    marginBottom: 20,
  },
  progressDot: {
    width: 12,
    height: 12,
    borderRadius: 6,
    marginHorizontal: 4,
  },
  skipButton: {
    alignSelf: 'flex-end',
    padding: 8,
  },
  skipText: {
    fontSize: 16,
    fontWeight: '500',
  },
  contentContainer: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    paddingVertical: 40,
  },
  iconContainer: {
    width: 160,
    height: 160,
    borderRadius: 80,
    justifyContent: 'center',
    alignItems: 'center',
    marginBottom: 40,
  },
  title: {
    fontSize: 28,
    fontWeight: 'bold',
    textAlign: 'center',
    marginBottom: 16,
  },
  description: {
    fontSize: 16,
    textAlign: 'center',
    lineHeight: 24,
    paddingHorizontal: 20,
  },
  profileSetup: {
    marginTop: 40,
    width: '100%',
  },
  inputLabel: {
    fontSize: 16,
    fontWeight: '600',
    textAlign: 'center',
    marginBottom: 16,
  },
  navigationContainer: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    paddingBottom: 40,
  },
  backButton: {
    flexDirection: 'row',
    alignItems: 'center',
    padding: 12,
  },
  backText: {
    fontSize: 16,
    fontWeight: '500',
    marginLeft: 4,
  },
  nextButton: {
    flex: 1,
    marginLeft: 20,
  },
});
