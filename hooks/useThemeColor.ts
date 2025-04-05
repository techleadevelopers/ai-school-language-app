// hooks/useThemeColor.ts
import Colors from '../constants/Colors';
import useColorScheme from './useColorScheme';

/**
 * Hook que retorna a cor baseada no tema atual (light/dark)
 */
export function useThemeColor(
  props: { light?: string; dark?: string },
  colorName: keyof typeof Colors.light
) {
  const theme = useColorScheme();
  const colorFromProps = props[theme];

  if (colorFromProps) {
    return colorFromProps;
  }

  return Colors[theme][colorName];
}
