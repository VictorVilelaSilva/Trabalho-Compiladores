program SomaDeDoisNumeros;

var
  num1, num2, soma: integer;

begin
  write('A soma de ', num1, ' e ', num2, ' é: ', soma);
  // Solicita ao usuário para inserir o primeiro número
  write('Digite o primeiro número: ');
  read(num1);

  // Solicita ao usuário para inserir o segundo número
  write('Digite o segundo número: ');
  read(num2);

  // Calcula a soma dos dois números
  soma := num1 + num2;

  // Exibe o resultado da soma
  write('A soma de ', num1, ' e ', num2, ' é: ', soma);

end.
