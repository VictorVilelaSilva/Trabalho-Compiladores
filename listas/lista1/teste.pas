program SomaDeDoisNumeros;
var
    num1, num2, soma: integer;
begin
    write('Digite o primeiro número: ');
    read(num1);
    
    write('Digite o segundo número: ');
    read(num2);
    
    soma := num1 + num2;
    
    write('A soma de ', num1, ' e ', num2, ' é: ', soma);
end.
