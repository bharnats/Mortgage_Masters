console.log('I work in the right directory')



function getSubmittedData() {
  submittedData = {
      Married: 1,
      Dependents: 0,
      Education: 1,
      Self_Employed: 0,
      ApplicantIncome: 9000,
      CoapplicantIncome: 2000,
      LoanAmount: 275,
      Loan_Amount_Term: 360,
      Credit_History: 1,
      Property_Area: 2
    };
  console.log(submittedData);
  return submittedData
};





function handleSubmit() {
  submittedData = getSubmittedData()
  console.log(submittedData);
  console.log(JSON.stringify(submittedData));
  var classifyURL = './submit';
  console.log(classifyURL);
  d3.json(classifyURL)
    .header('Content-Type', 'application/json')
    .post(JSON.stringify(submittedData), function(error, data) {
      console.log(error);
      console.log(data);
   })

  console.log('testing complete');
}

handleSubmit()
