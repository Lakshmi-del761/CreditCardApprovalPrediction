document.getElementById("predictionForm").addEventListener("submit", async function(e){

    e.preventDefault();

    const predictBtn = document.getElementById("predictBtn");
    const loading = document.getElementById("loading");
    const result = document.getElementById("result");

    predictBtn.disabled = true;
    loading.style.display = "block";
    result.style.display = "none";

    const formData = {

        Gender: Number(document.getElementById("Gender").value),
        Age: Number(document.getElementById("Age").value),
        Debt: Number(document.getElementById("Debt").value),
        Married: Number(document.getElementById("Married").value),
        BankCustomer: Number(document.getElementById("BankCustomer").value),

        Industry: document.getElementById("Industry").value,
        Ethnicity: document.getElementById("Ethnicity").value,

        YearsEmployed: Number(document.getElementById("YearsEmployed").value),

        PriorDefault: Number(document.getElementById("PriorDefault").value),
        Employed: Number(document.getElementById("Employed").value),

        CreditScore: Number(document.getElementById("CreditScore").value),

        DriversLicense: Number(document.getElementById("DriversLicense").value),

        Citizen: document.getElementById("Citizen").value,

        ZipCode: Number(document.getElementById("ZipCode").value),

        Income: Number(document.getElementById("Income").value)

    };

    try{

        const response = await fetch("/predict",{

            method:"POST",

            headers:{
                "Content-Type":"application/json"
            },

            body:JSON.stringify(formData)

        });

        const data = await response.json();

        loading.style.display = "none";

        result.style.display = "block";

        if(data.prediction === "Approved"){

            result.className = "result-card approved";

            result.innerHTML = `
                <h3>✅ Credit Card Approved</h3>
                <p>The applicant is likely eligible for credit card approval.</p>
            `;

        }
        else{

            result.className = "result-card rejected";

            result.innerHTML = `
                <h3>❌ Credit Card Rejected</h3>
                <p>The applicant is unlikely to receive approval.</p>
            `;

        }

    }
    catch(error){

        loading.style.display = "none";

        result.style.display = "block";

        result.className = "result-card rejected";

        result.innerHTML = `
            <h3>Server Error</h3>
            <p>${error}</p>
        `;

    }

    predictBtn.disabled = false;

});