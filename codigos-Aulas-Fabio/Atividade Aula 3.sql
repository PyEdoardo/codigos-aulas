alter procedure proc_comissoes
	@codVendedor int
as
begin
	declare @somaMesAtual float, @somaMesAnterior float;
	set @somaMesAtual = (
		select sum(valorComissao) 
        from Comissao 
        where codVendedor = @codVendedor 
          and month(dataVenda) = month(getDate()) 
          and year(dataVenda) = year(getDate())
	);

	print @somaMesAtual;

	set @somaMesAnterior = (
        select sum(valorComissao) 
        from Comissao 
        where codVendedor = @codVendedor 
          and month(dataVenda) = month(dateAdd(month, -1, getDate()))
          and year(dataVenda) = year(dateAdd(month, -1, getDate()))
    );

	if @somaMesAnterior is null
		set @somaMesAnterior = 0

	if @somaMesAtual > @somaMesAnterior
		print 'A Soma do Mês Atual é Maior que a do Mês Anterior';
	else
		print 'A Soma do Mês Atual é inferior que a do Mês Anterior';
end
drop procedure proc_comissoes
exec proc_comissoes @codVendedor = 1
go

create trigger tr_addComissao
on Venda
for insert
as
begin
	declare @valorComissaoTemp float, @codVendedorTemp int, @dataVendaTemp date;
	set @valorComissaoTemp = (select totalVenda from inserted) * 0.01;
	set @codVendedorTemp = (select codVendedor from inserted);
	set @dataVendaTemp = (select dataVenda from inserted);
	insert into Comissao (codVendedor, dataVenda, valorComissao)
	values (@codVendedorTemp, @dataVendaTemp, @valorComissaoTemp);
end

drop trigger tr_addComissao


insert into Cliente (nomeCliente) values ('Edoardo');
insert into Vendedor (nomeVendedor) values ('João');

insert into Venda (codCliente, codVendedor, dataVenda, totalVenda) values (1, 1, getDate(), 1000)

select * from Comissao