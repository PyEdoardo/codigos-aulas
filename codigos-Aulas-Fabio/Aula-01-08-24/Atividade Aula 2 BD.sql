/*
create procedure proc_adicionarProduto
	@nomeProduto varchar (100),
	@precoProduto float
	as
	begin
		insert into Produto (nomeProduto, precoProduto)
		values (@nomeProduto, @precoProduto)
	end

create procedure proc_adicionarProduto2
	@nomeProduto varchar (100) = null, @precoProduto float = null,
	@mensagem varchar (50) OUTPUT, @opcao int = null
	as
	begin
		if (@opcao = 1) begin
			insert into Produto (nomeProduto, precoProduto)
			values (@nomeProduto, @precoProduto);
			set @mensagem = 'O Registro foi inserido!';
		end
		else begin
			select * from Produto;
			set @mensagem = 'Resultado da Consulta!';
		end
	end
*/

create procedure desafio1
	@frase varchar (150)
	as
	begin
		declare
		@cont int = 1;
		while @cont <= len(@frase)
		begin
			print(substring(@frase, @cont, 1))
			set @cont = @cont + 1
		end
	end
go
create procedure desafio2
	@frase varchar (150)
	as
	begin
		declare
		@cont int = 1
		while @cont <= len(@frase)
		begin
			if @cont % 2 = 0 begin
				print(substring(@frase, @cont, 1));
			end
			set @cont = @cont + 1;
		end
	end
go
create procedure desafio3
	@cpf varchar (14),
	@cpfFormatado varchar(14) output
	as
	begin
		set @cpfFormatado = substring(@cpf, 1, 3) + '.'
							+ substring(@cpf, 4, 3) + '.'
							+ substring(@cpf, 7, 3) + '-'
							+ substring(@cpf, 10, 2);
	end

drop procedure desafio2
drop procedure desafio3

/*
exec proc_adicionarProduto 'Arroz', 18;
exec proc_adicionarProduto 'Macarrão', 9.99; 

declare
	@msg varchar(50)

exec proc_adicionarProduto2 @nomeProduto = 'Bolo de Banana', @precoProduto = 21.99, @mensagem = @msg output, @opcao = 2;
exec proc_adicionarProduto2 @mensagem = @msg output, @opcao = 2;
print(@msg);

select * from Produto;
*/

exec desafio1 @frase = 'Edoardo'
exec desafio2 @frase = 'Edoardo'

declare
	@cpf2 varchar(14);
exec desafio3 '11122233344', @cpfFormatado = @cpf2 output
print(@cpf2)
