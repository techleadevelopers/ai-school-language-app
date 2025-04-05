// 📁 screens/LoginScreen.tsx
import React, { useState } from 'react';
import { View, TextInput, Image, StyleSheet, KeyboardAvoidingView, Platform } from 'react-native';
import PrimaryButton from '@/components/PrimaryButton';
import Typography from '@/components/Typography';

export default function LoginScreen() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleLogin = () => {
    if (!email || !password) {
      alert('Por favor, preencha todos os campos.');
      return;
    }

    // Aqui você pode integrar com o Firebase/Auth mais tarde
    alert(`Login com: ${email}`);
  };

  return (
    <KeyboardAvoidingView
      behavior={Platform.OS === 'ios' ? 'padding' : undefined}
      style={styles.container}
    >
      <View style={styles.overlay}>
        <Image source={require('@/assets/images/logo.png')} style={styles.logo} />
        <Typography type="title" style={styles.title}>Bilingui-AI</Typography>

        <TextInput
          placeholder="Email ou nome de usuário"
          placeholderTextColor="#aaa"
          style={styles.input}
          value={email}
          onChangeText={setEmail}
          autoCapitalize="none"
          keyboardType="email-address"
        />

        <TextInput
          placeholder="Senha"
          placeholderTextColor="#aaa"
          style={styles.input}
          value={password}
          onChangeText={setPassword}
          secureTextEntry
        />

        <PrimaryButton title="Entrar" onPress={handleLogin} />

        <Typography type="secondary" style={styles.footer}>
          Esqueceu sua senha?
        </Typography>
      </View>
    </KeyboardAvoidingView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#000',
    justifyContent: 'center',
    alignItems: 'center',
  },
  overlay: {
    width: '90%',
    backgroundColor: 'rgba(0,0,0,0.9)',
    padding: 24,
    borderRadius: 16,
    alignItems: 'center',
  },
  logo: {
    width: 120,
    height: 120,
    marginBottom: 16,
  },
  title: {
    color: '#00f5c4',
    fontSize: 24,
    marginBottom: 24,
  },
  input: {
    width: '100%',
    backgroundColor: '#1a1a1a',
    borderRadius: 8,
    padding: 14,
    color: '#fff',
    fontSize: 16,
    marginBottom: 16,
    borderWidth: 1,
    borderColor: '#333',
  },
  footer: {
    marginTop: 12,
    color: '#999',
  },
});
