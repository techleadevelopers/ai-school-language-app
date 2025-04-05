// 📁 screens/LessonScreen.tsx
import { View, StyleSheet, FlatList } from 'react-native';
import { useState, useEffect } from 'react';
import Container from '@/components/Container';
import Typography from '@/components/Typography';
import PrimaryButton from '@/components/PrimaryButton';
import { getLesson } from '@/service/api';

interface Question {
  id: string;
  question: string;
  options: string[];
  answer: string;
}

interface LessonResponse {
  questions: Question[];
}

export default function LessonScreen() {
  const [questions, setQuestions] = useState<Question[]>([]);
  const [selected, setSelected] = useState<{ [key: string]: string }>({});
  const [feedback, setFeedback] = useState<{ [key: string]: string }>({});

  useEffect(() => {
    fetchLesson();
  }, []);

  const fetchLesson = async () => {
    try {
      const res: LessonResponse = await getLesson('en', 'basic'); // 👈 Tipagem aqui
      setQuestions(res.questions);
    } catch (err) {
      console.error('Erro ao carregar lições:', err);
    }
  };

  const submitAnswer = (questionId: string, option: string) => {
    setSelected((prev) => ({ ...prev, [questionId]: option }));
    const correct = questions.find(q => q.id === questionId)?.answer;
    setFeedback((prev) => ({
      ...prev,
      [questionId]: correct === option ? '✅ Correto!' : `❌ Errado. Resposta: ${correct}`,
    }));
  };

  return (
    <Container>
      <Typography type="headline">📚 Aula de Hoje</Typography>
      <FlatList
        data={questions}
        keyExtractor={(item) => item.id}
        renderItem={({ item }) => (
          <View style={styles.questionBlock}>
            <Typography>{item.question}</Typography>
            {item.options.map((opt) => (
              <PrimaryButton
                key={opt}
                title={opt}
                onPress={() => submitAnswer(item.id, opt)}
                style={selected[item.id] === opt ? styles.selected : undefined}
              />
            ))}
            {feedback[item.id] && (
              <Typography style={styles.feedback}>{feedback[item.id]}</Typography>
            )}
          </View>
        )}
      />
    </Container>
  );
}

const styles = StyleSheet.create({
  questionBlock: {
    marginBottom: 24,
    padding: 16,
    borderRadius: 12,
    backgroundColor: '#f4f4f4',
  },
  feedback: {
    marginTop: 8,
    fontStyle: 'italic',
  },
  selected: {
    backgroundColor: '#B2E4F5',
  },
});
