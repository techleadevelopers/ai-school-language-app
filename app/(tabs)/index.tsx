// 📁 app/(tabs)/index.tsx
import { StyleSheet, Image, Platform } from 'react-native';
import ParallaxScrollView from '@/components/ParallaxScrollView';
import Container from '@/components/Container';
import Typography from '@/components/Typography';

export default function HomeScreen() {
  return (
    <ParallaxScrollView
      headerBackgroundColor={{ light: '#B0E0E6', dark: '#1A1D2B' }}
      headerImage={
        <Image
          source={require('@/assets/images/logo.png')}
          style={styles.logo}
          resizeMode="contain"
        />
      }
    >
      <Container>
        <Typography type="headline">Bem-vindo ao Bilingui-AI 👋</Typography>
        <Typography>
          Aprenda idiomas de forma prática com IA local, correções em tempo real e desafios gamificados.
        </Typography>

        <Typography type="headline">📘 Como começar:</Typography>
        <Typography>
          1️⃣ Vá para a aba <Typography style={{ fontWeight: 'bold' }}>Explorar</Typography> para praticar sua fala{'\n'}
          2️⃣ Toque no microfone e diga uma frase{'\n'}
          3️⃣ Veja o feedback da IA com sugestões de melhoria
        </Typography>

        <Typography type="headline">🚀 Dicas</Typography>
        <Typography>
          Toque nos ícones abaixo para acessar rankings, lições e histórico.
        </Typography>
      </Container>
    </ParallaxScrollView>
  );
}

const styles = StyleSheet.create({
  logo: {
    height: 200,
    width: 200,
    alignSelf: 'center',
    marginTop: Platform.OS === 'ios' ? 60 : 40,
  },
});
