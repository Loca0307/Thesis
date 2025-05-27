        li.className = 'todo text-black text-xl border border-white bg-white px-3 py-1 my-1 rounded-md w-full'
        li.textContent = input.value

        const deleteBtn = document.createElement("button")
        deleteBtn.className = "text-white bg-[#DD4230] px-3 py-2 rounded-md"
        deleteBtn.innerHTML = '<i class="fa-solid fa-trash"></i>'

        deleteBtn.addEventListener('click', function(){
            listContainer.removeChild(todoDiv)
        })

        todoDiv.appendChild(li)
        todoDiv.appendChild(deleteBtn)

        listContainer.appendChild(todoDiv)

        input.value = ""