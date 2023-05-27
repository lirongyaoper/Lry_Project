const container = document.querySelector(".container");

// 创建一个随机数组
const arr = [];
for(let i = 0; i < 10; i++){
    arr.push(Math.floor(Math.random() * 100 + 5));
}

// 用数组创建矩形条元素
arr.forEach((value) => {
    const bar = document.createElement("div");
    bar.classList.add("bar");
    bar.style.height = `${value * 3}px`;
    container.appendChild(bar);
});


async function bubbleSortAnimation() {
    const bars = document.querySelectorAll(".bar");
  
    for (let i = 0; i < bars.length; i++) {
        for (let j = 0; j < bars.length - i - 1; j++) {
            bars[j].style.backgroundColor = "red";
            bars[j + 1].style.backgroundColor = "red";
      
            await new Promise((resolve) =>
                setTimeout(() => {
                resolve();
                }, 2000)
            );
      
            if (parseInt(bars[j].style.height) > parseInt(bars[j + 1].style.height)) {
                // 交换高度
                let temp = bars[j].style.height;
                bars[j].style.height = bars[j + 1].style.height;
                bars[j + 1].style.height = temp;
            }
      
            bars[j].style.backgroundColor = "dodgerblue";
            bars[j + 1].style.backgroundColor = "dodgerblue";
        }
    }
}