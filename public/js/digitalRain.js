// 检查客户端是否为手机
function checkClient() {
    let userAgentInfo = navigator.userAgent;
    const AGENTS = ["Android", "iPhone", "SymbianOS", "Windows Phone"];
    for (let i = 0; i < AGENTS.length; i++) {
        if (userAgentInfo.indexOf(AGENTS[i]) > 0) {
            // 手机访问
            return true;
        };
    };
    return false;
};

/**
 * DigitalRain (代码雨)
 * version : 1.0
*/

class DigitalRain {

    // 设置参数
    static fontsize = 16;
    static columns = 0;
    static dropLine = [];
    width = 0;
    height = 0;
    static ctx = 0;
    timer = 0;

    constructor(canvas) {
        this.canvas = canvas;
        DigitalRain.ctx = this.canvas.getContext("2d");

    };

    static checkClient() {
        if (checkClient()) {
            DigitalRain.fontsize = 12;
        } else {
            DigitalRain.fontsize = 18;
        };
        return checkClient();
    };

    static init = (() => {
        DigitalRain.checkClient();
        DigitalRain.width = document.documentElement.clientWidth;
        DigitalRain.height = document.documentElement.clientHeight;
        DigitalRain.columns = Math.ceil(DigitalRain.width / DigitalRain.fontsize);
        for (let i = 0; i < DigitalRain.columns; i++) {
            DigitalRain.dropLine[i] = 0;
        };
        return DigitalRain.dropLine;
    })();

    static rain() {
        DigitalRain.ctx.fillStyle = "rgba(0, 0, 0, 0.08)";   //设置透明度，逐渐覆盖之前的数字
        DigitalRain.ctx.fillRect(0, 0, DigitalRain.width, DigitalRain.height);       //填充画布
        DigitalRain.ctx.fillStyle = "#00FFFF";
        DigitalRain.ctx.font = DigitalRain.fontsize + "px Simsun";

        for (let i = 0; i < DigitalRain.columns; i++) {
            let figure = Math.floor(Math.random() * 10);  //生成0~9的伪随机数

            /*绘制数字(核心部分)*/
            DigitalRain.ctx.fillText(figure, (i * DigitalRain.fontsize), (DigitalRain.dropLine[i] * DigitalRain.fontsize));

            if (DigitalRain.dropLine[i] * DigitalRain.fontsize > DigitalRain.height || Math.random() > 0.95) {
                DigitalRain.dropLine[i] = 0;
            }
            DigitalRain.dropLine[i]++;
        };
    };

    run() {
        DigitalRain.init;
        if (this.canvas.getContext) {
            DigitalRain.timer = setInterval(DigitalRain.rain, 30);
        };
    };

    stop() {
        clearInterval(DigitalRain.timer);
    };
};
