function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

document.addEventListener("DOMContentLoaded", async (event) => {  
    try{                
        if (window.screen.width >= 300 && window.screen.width <= 670){            
            let typingLineOneMobile = document.querySelector('#typingLineOneMobile');
            let typingLineTwoMobile = document.querySelector('#typingLineTwoMobile');

            await sleep(1500);        
            typingLineOneMobile.classList.add('typing-animation');
            typingLineOneMobile.style.display = 'block'
            typingLineOneMobile.style.width = '100%'
            await sleep(2500);
            typingLineOneMobile.classList.remove('typing-animation');
            await sleep(500);
            typingLineTwoMobile.style.display = 'block'
            typingLineTwoMobile.classList.add('typing-animation');
        } else{
            let typingLineOne = document.querySelector('#typingLineOne');
            let typingLineTwo = document.querySelector('#typingLineTwo');

            await sleep(1500);        
            typingLineOne.classList.add('typing-animation');
            typingLineOne.style.display = 'block'
            typingLineOne.style.width = '100%'
            await sleep(2500);
            typingLineOne.classList.remove('typing-animation');
            await sleep(500);
            typingLineTwo.style.display = 'block'
            typingLineTwo.classList.add('typing-animation');
        }
    } catch {
        //
    }    
});