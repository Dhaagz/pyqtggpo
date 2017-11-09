var boost_price = document.getElementById("boost_price");
var boost_submit = document.getElementById("boost_submit");
//var boost_selectors = document.getElementsByClassName("rank_select");

var initialrank_select = document.getElementById("initialrank_select");
var wantedrank_select = document.getElementById("wantedrank_select");

wantedrank_select.onchange = function(){
	updateRank();
}
initialrank_select.onchange = function(){
	updateRank();
}

function updateRank(){
	var price_diff = rank_prices[wantedrank_select.value] - rank_prices[initialrank_select.value];
	if( price_diff > 0 ){
		boost_price.innerHTML=price_diff + " €";
		boost_submit.disabled = false;			
	}
	else{
		boost_price.innerHTML="Choisissez un rang supérieur à l'actuel."
		boost_submit.disabled = true;
	}
}
