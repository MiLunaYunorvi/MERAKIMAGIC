var codigos_list = ['059066','077999','215133','283897',
   '401419','466461','726100','938563'];
var CodeContainer = document.querySelector('.codeContainer')

function renderCodigos(codigos_list){
    const lista = document.createElement('ol');
    lista.classList.add('CodeList');

    for (codigo of codigos_list){
        
        const item = document.createElement('li');
        item.innerText = codigo;
        item.classList.add('ItemCodeList');

        lista.append(item);
    }
    CodeContainer.append(lista);
}

renderCodigos(codigos_list);