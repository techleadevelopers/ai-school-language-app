// 📁 app/_layout.tsx - Layout Global
import { useEffect, useState } from 'react';
import { Slot, Redirect } from 'expo-router';
import { SafeAreaProvider } from 'react-native-safe-area-context';
import { StatusBar } from 'expo-status-bar';
import useColorScheme from '../hooks/useColorScheme';
import { ThemeProvider } from '@react-navigation/native';
import Colors from '../constants/Colors';

export default function RootLayout() {
  const colorScheme: 'light' | 'dark' = useColorScheme();
  const themeColors = Colors[colorScheme];

  const [isLoggedIn, setIsLoggedIn] = useState(false); // 👈 Simule login
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // 👉 Trocar isso por lógica real depois (e.g. AsyncStorage, Firebase, etc)
    const checkAuth = async () => {
      // await AsyncStorage.getItem('userToken') etc...
      setIsLoggedIn(false); // coloque true se quiser pular o login
      setLoading(false);
    };
    checkAuth();
  }, []);

  if (loading) return null; // Pode adicionar um splash ou loader

  if (!isLoggedIn) {
    return <Redirect href="/login" />;
  }

  return (
    <SafeAreaProvider>
      <ThemeProvider
        value={{
          dark: colorScheme === 'dark',
          colors: themeColors,
        }}
      >
        <StatusBar style={colorScheme === 'dark' ? 'light' : 'dark'} />
        <Slot />
      </ThemeProvider>
    </SafeAreaProvider>
  );
}
