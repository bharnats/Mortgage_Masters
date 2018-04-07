


function getSubmittedData() {
  var MarriedValue = document.getElementById("Married").value;
  var DependentsValue = document.getElementById("Dependents").value;
  var EducationValue = document.getElementById("Education").value;
  var Self_EmployedValue = document.getElementById("Self_Employed").value;
  var ApplicantIncomeValue = document.getElementById("ApplicantIncome").value;
  var CoapplicantIncomeValue = document.getElementById("CoapplicantIncome").value;
  var LoanAmountValue = document.getElementById("LoanAmount").value;
  var Loan_Amount_TermValue = document.getElementById("Loan_Amount_Term").value;
  var Credit_HistoryValue = document.getElementById("Credit_History").value;
  var Property_AreaValue = document.getElementById("Property_Area").value;
  console.log(`MarriedValue ${MarriedValue}`);
  console.log(`DependentsValue ${DependentsValue}`);
  console.log(`EducationValue ${EducationValue}`);
  console.log(`Self_EmployedValue ${Self_EmployedValue}`);
  console.log(`ApplicantIncomeValue ${ApplicantIncomeValue}`);
  console.log(`CoapplicantIncomeValue ${CoapplicantIncomeValue}`);
  console.log(`LoanAmountValue ${LoanAmountValue}`);
  console.log(`Loan_Amount_TermValue ${Loan_Amount_TermValue}`);
  console.log(`Credit_HistoryValue ${Credit_HistoryValue}`);
  console.log(`Property_AreaValue ${Property_AreaValue}`);
  var submittedData = {
        Married: +MarriedValue,
        Dependents: +DependentsValue,
        Education: +EducationValue,
        Self_Employed: +Self_EmployedValue,
        ApplicantIncome: +ApplicantIncomeValue,
        CoapplicantIncome: +CoapplicantIncomeValue,
        LoanAmount: +LoanAmountValue,
        Loan_Amount_Term: +Loan_Amount_TermValue,
        Credit_History: +Credit_HistoryValue,
        Property_Area: +Property_AreaValue
    };
  console.log(submittedData);
  return submittedData
};



function updateDisplayedLoanStatus(error, data) {
  console.log(error);
  console.log(data);
  if (data["prediction"] === "approved") {
    var newImgLocation = "static/images/approve.png";
  } else {
    var newImgLocation = "static/images/deny.png";
  }
  document.getElementById("model-classificaion-text").innerHTML = data['prediction_text'];
  document.getElementById("model-classificaion-img").src = newImgLocation;
  document.getElementById("mortgage-submit").innerHTML = "Resubmit Loan Application";
}



function provideLoadingFeedback() {
  document.getElementById("model-classificaion-text").innerHTML = "Reviewing your application...";
  document.getElementById("model-classificaion-img").src = "static/images/load.gif";
}

function handleSubmit() {
  provideLoadingFeedback();
  var submittedData = getSubmittedData();
  var classifyURL = './submit';
  d3.json(classifyURL)
    .header('Content-Type', 'application/json')
    .post(JSON.stringify(submittedData), updateDisplayedLoanStatus)
}


function handleRefresh() {
  document.getElementById("mortgage-form").reset();
  document.getElementById("model-classificaion-text").innerHTML = "Use the form above to submit your data";
  document.getElementById("model-classificaion-img").src = "static/images/submit.png"
  document.getElementById("mortgage-submit").innerHTML = "Submit Loan Application";
}




var mortgageSubmit = document.querySelector("#mortgage-submit");
mortgageSubmit.addEventListener("click", handleSubmit);

var mortgageRefresh = document.querySelector("#mortgage-refresh");
mortgageRefresh.addEventListener("click", handleRefresh);
