// 📁 service/api.ts
import axios from 'axios';

interface Question {
  id: string;
  question: string;
  options: string[];
  answer: string;
}

interface LessonResponse {
  questions: Question[];
}

export const getLesson = async (language: string, level: string): Promise<LessonResponse> => {
  const res = await axios.get<LessonResponse>(`http://localhost:8000/llm/lesson?language=${language}&level=${level}`);
  return res.data;
};
