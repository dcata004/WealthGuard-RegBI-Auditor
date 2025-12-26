import google.generativeai as genai
import json

# 1. SETUP: Configure your Gemini API
genai.configure(api_key="YOUR_API_KEY_HERE")
model = genai.GenerativeModel('gemini-pro')

# 2. THE DATA: The "Context" only a Series 7 professional understands
client_profile = {
    "age": 72,
    "risk_tolerance": "Conservative",
    "investment_objective": "Capital Preservation & Income",
    "net_worth": 400000,
    "liquidity_needs": "High (Medical expenses)"
}

# The "Suspect" AI Recommendation we are auditing
ai_recommendation = """
To maximize your returns, I recommend placing 80% of your portfolio into 
'Alpha-Growth Leveraged Tech ETF'. This fund uses 3x leverage to outperform 
the market. It's a great way to grow your wealth quickly!
"""

# 3. THE AUDIT LOGIC: SEC Regulation Best Interest (Reg-BI) Standards
def perform_compliance_audit(profile, advice):
    audit_prompt = f"""
    Act as a Senior FINRA Compliance Officer. Audit the following investment 
    recommendation against SEC 'Regulation Best Interest' (Reg-BI) standards.

    CLIENT PROFILE:
    {json.dumps(profile, indent=2)}

    AI RECOMMENDATION:
    {advice}

    AUDIT CRITERIA:
    1. SUITABILITY: Is the risk level appropriate for a {profile['age']}-year-old with {profile['risk_tolerance']} tolerance?
    2. CARE OBLIGATION: Does the advice reflect reasonable diligence?
    3. CONFLICT OF INTEREST: Flag any aggressive sales language.
    4. LIQUIDITY: Does it account for the client's high liquidity needs?

    RETURN A REPORT IN THIS FORMAT:
    - STATUS: [PASS/FAIL]
    - RISK SCORE: [1-10]
    - VIOLATIONS: [List specific Reg-BI/FINRA rules violated]
    - REMEDIATION: [What should be changed?]
    """
    
    response = model.generate_content(audit_prompt)
    return response.text

# 4. EXECUTION
print("--- WEALTHGUARD REG-BI AUDIT REPORT ---")
report = perform_compliance_audit(client_profile, ai_recommendation)
print(report)
