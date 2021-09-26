

$( function() {
    var registerEffect,  loginEffect= false;
    // run the currently selected effect
    function runEffectRegister() {
    // get effect type from
    var selectedEffect = "slide"

    // Run the effect
    $( "#registerEffect" ).toggle( selectedEffect);
    registerEffect = true;
    };

    function runEffectLogin() {
        // get effect type from
        var selectedEffect = "slide"
    
        // Run the effect
        $( "#loginEffect" ).toggle( selectedEffect);
        loginEffect = true;
        };
    



    // Set effect from select menu value
    $( "#registerBotton" ).on( "click", function() {
    runEffectRegister();
    if (loginEffect){
        loginEffect =false;
        $( "#loginEffect" ).hide();
    }
    });
    $( "#loginBotton" ).on( "click", function() {
        runEffectLogin();
        registerEffect = false
        $( "#registerEffect" ).hide();
    });
    $( "#registerEffect" ).hide();
    $( "#loginEffect" ).hide();
    
} );


