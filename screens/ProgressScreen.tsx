// screens/ProgressScreen.tsx
import { View, ScrollView, StyleSheet } from 'react-native';
import  Typography  from '@/components/Typography';
import { XPProgressBar } from '@/components/XPProgressBar';
import  Container  from '@/components/Container';
import  PrimaryButton  from '@/components/PrimaryButton';

export default function ProgressScreen() {
  return (
    <ScrollView>
      <Container>
        <Typography type="title">Seu Progresso</Typography>
        <Typography>
          Acompanhe sua jornada de aprendizado. Você pode visualizar seu XP total, nível atual e conquistas.
        </Typography>

        {/* Exemplo de progresso */}
        <XPProgressBar xp={250} level={3} />

        {/* Medalhas ou conquistas */}
        <View style={styles.achievementsSection}>
          <Typography type="headline">Conquistas</Typography>
          <View style={styles.badges}>
            <View style={styles.badge} />
            <View style={styles.badge} />
            <View style={styles.badge} />
          </View>
        </View>

        {/* Botão para exportar histórico */}
        <PrimaryButton title="Exportar Histórico (PDF)" onPress={() => alert('Função em breve!')} />
      </Container>
    </ScrollView>
  );
}

const styles = StyleSheet.create({
  achievementsSection: {
    marginTop: 24,
  },
  badges: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    marginVertical: 16,
  },
  badge: {
    width: 80,
    height: 80,
    backgroundColor: '#C6E2FF',
    borderRadius: 40,
  },
});