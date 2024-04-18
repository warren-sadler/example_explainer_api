from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

class UserContext(BaseModel):
    name: str
    insuranceProvider: str
    concerns: list[str]

class ProviderFinancials(BaseModel):
    sessionFee: float
    offersSlidingScale: bool
    paymentMethods: list[str]

class ProviderQualifications(BaseModel):
    yearsOfExperience: int

class ProviderClientFocus(BaseModel):
    ageGroups: list[str]
    communities: list[str]
    ethnicity: list[str]
    languages: list[str]

class ProviderContext(BaseModel):
    name: str
    credentials: list[str]
    bio: str
    isSupervised: bool
    specialties: list[str]
    typesOfTherapy: list[str]
    location: str
    financials: ProviderFinancials
    qualifications: ProviderQualifications
    clientFocus: ProviderClientFocus

class Request(BaseModel):
    user: UserContext
    provider: ProviderContext


class Response(BaseModel):
    prompt: str
    user: UserContext
    provider: ProviderContext
    explanation: str

prompt = f"""
You are a care navigator, skilled in helping individuals find the right mental health provider.
Your job is to help the user understand the mental health provider's context and help them make an informed decision.
You are to be empathetic and understanding of the user's concerns and needs, while being terse and informative.
---
<UserContext>
    <Name></Name>
    <InsuranceProvider></InsuranceProvider>
    <Concerns>
        <Concern></Concern>
    </Concerns>
</UserContext>
---
<ProviderContext>
</ProviderContext>
"""


@app.get("/ping")
def index(): # handler function for the route
    return {"status": "ok"}

@app.post("/explain")
def explain(request: Request):
    # do some processing
    # send request to the model
    # get the response from the model
    # return the response
    response = Response(
        prompt=prompt,
        user=request.user,
        provider=request.provider,
        explanation="This is the explanation"
    )
    return response