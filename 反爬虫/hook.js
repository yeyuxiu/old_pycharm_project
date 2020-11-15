// hook stringify
(function(){
	'use strict';
	//将 JSON stringify 赋值给一个变量
	var stringify = JSON.stringify;
	JSON.stringify = funciton(inpt){
			// 为所欲为部分开始
			console.log("stringify -> ", inpt);
			debugger; // 自动暂停，便于我们观察
			//为所欲为结束
		// 将原函数返回
		return stringify(inpt)
		{
})();
// hook JSON.parse、atob、btoa , windos."asc"
(function() {
	'user strict';
	var pre = window._pt_;
	Object.defineProperty(window,"_pt_",{
		get: function(){
				console.log("pre: ".pre)
		},
		set: function(var){
			console.log("_pt_: ", var);
			debugger;
			pre = val;
			return pre;
	}
})
})();
//调用方和原函数的是直接关联的，调用方调用原函数，原函数启动执行。我们在它们之间加了一个 hook 函数，hook 到传入的参数后为所欲为，但为了保证系统正常运行，我们在得到参数后便返回原函数。