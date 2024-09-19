document.addEventListener('DOMContentLoaded', function (){
    const buttons = document.querySelectorAll('#edit');
    buttons.forEach(function(button){
        button.addEventListener('click', () => {
            id = button.dataset.id
            const text_area = document.createElement('textarea');
            text_area.setAttribute('class' , 'form-control');
            text_area.setAttribute('rows' , '3');
            
            const content = document.querySelector(`[data-id="${id}"][id="content"]`);
            content.innerHTML = '';
            content.appendChild(text_area);
            const save = document.querySelector(`[data-id="${id}"][id="save"]`);
            document.querySelector(`[data-id="${id}"][id="save"]`).style.display = 'block';
            save.onclick = function(){
                const text = text_area.value;
                content.innerHTML = '';
                content.innerHTML = text;
                save.style.display = 'none';
            }
        })
    })
    
})