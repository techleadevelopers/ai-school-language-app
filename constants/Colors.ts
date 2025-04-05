// constants/Colors.ts

type ThemeColors = {
  background: string;
  primary: string;
  secondary: string;
  accent: string;
  text: string;
  card: string;
};

const Colors: Record<'light' | 'dark', ThemeColors> = {
  light: {
    background: '#F9FAFB',
    primary: '#2E90FA',
    secondary: '#38BDF8',
    accent: '#FF6F00',
    text: '#1F2937',
    card: '#FFFFFF',
  },
  dark: {
    background: '#0F172A',
    primary: '#3B82F6',
    secondary: '#60A5FA',
    accent: '#FF8C00',
    text: '#F8FAFC',
    card: '#1E293B',
  },
};

export default Colors;
