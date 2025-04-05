// 📁 app/(tabs)/_layout.tsx
import { Tabs } from 'expo-router';
import { Ionicons } from '@expo/vector-icons';
import Colors from '../../constants/Colors';
import useColorScheme from '../../hooks/useColorScheme';

export default function TabLayout() {
  const colorScheme: 'light' | 'dark' = useColorScheme();
  const themeColors = Colors[colorScheme];

  return (
    <Tabs
      screenOptions={{
        headerShown: false,
        tabBarActiveTintColor: themeColors.primary,
        tabBarStyle: {
          backgroundColor: themeColors.background,
          borderTopColor: themeColors.secondary,
        },
      }}
    >
      <Tabs.Screen
        name="index"
        options={{
          title: 'Início',
          tabBarIcon: ({ color, size }: { color: string; size: number }) => (
            <Ionicons name="home-outline" color={color} size={size} />
          ),
        }}
      />
      <Tabs.Screen
        name="explore"
        options={{
          title: 'Explorar',
          tabBarIcon: ({ color, size }: { color: string; size: number }) => (
            <Ionicons name="mic-outline" color={color} size={size} />
          ),
        }}
      />
    </Tabs>
  );
}
