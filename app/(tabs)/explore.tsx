// 📁 app/(tabs)/explore.tsx
import { StyleSheet, Platform } from 'react-native';
import ParallaxScrollView from '@/components/ParallaxScrollView';
import Typography from '@/components/Typography';
import Container from '@/components/Container';
import FeedbackBox from '@/components/FeedbackBox';
import { XPProgressBar } from '@/components/XPProgressBar';
import { VoiceButton } from '@/components/VoiceButton';

export default function ExploreScreen() {
  return (
    <ParallaxScrollView
      headerBackgroundColor={{ light: '#E1F3FF', dark: '#1B1F23' }}
      headerImage={
        <Typography type="title" style={styles.headerText}>
          🎤 Fale para praticar
        </Typography>
      }
    >
      <Container>
        <Typography type="headline">Vamos praticar!</Typography>
        <Typography>
          Pressione o botão abaixo e fale uma frase. Vamos transcrever, corrigir e te mostrar como melhorar.
        </Typography>
        <VoiceButton />
        <FeedbackBox />
        <XPProgressBar xp={50} level={1} />
      </Container>
    </ParallaxScrollView>
  );
}

const styles = StyleSheet.create({
  headerText: {
    fontSize: 32,
    fontWeight: 'bold',
    alignSelf: 'center',
    marginTop: Platform.OS === 'ios' ? 80 : 60,
  },
});
