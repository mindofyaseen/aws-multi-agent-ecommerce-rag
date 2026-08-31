# NovaMart Bedrock Knowledge Bases — Live Parallel Retrieval Evidence

**Execution Timestamp:** 2026-08-31T12:55:51.303333+00:00
**Region:** `us-east-1`
**Embedding Model:** Amazon Titan Embed Text v2
**Vector Backing Store:** Amazon S3 Vectors

---

## Returns Policy Knowledge Base (`HHE4AWZZLY`)
- **Natural Language Query:** `What is the return window for Premium customers vs Standard customers?`
- **Retrieved Passages Count:** 3

### Passage 1 (Relevance Score: `0.7237`)
- **Source S3 URI:** `s3://udacity-agentcore-policy-docs-237657481511-d7be52e0/policies/returns/customer_tiers.txt`
- **Content:**
```text
NovaMart Customer Tier Program ================================ Last Updated: January 2025  TIER OVERVIEW NovaMart offers two customer tiers: Standard and Premium.  STANDARD TIER - Default tier for all new customers - 30-day return window - Standard shipping rates apply - 1-year warranty on electronics - Standard customer support response time: 24-48 hours  PREMIUM TIER Requirements: Spend $500+ in a calendar year OR place 20+ orders in a calendar year. Benefits: - Extended 60-day return window - Free expedited shipping on all orders - 3-year warranty on electronics - Priority customer support: response within 4 hours - Early access to sales and new product launches - Dedicated account manager for orders over $500  HOW TO UPGRADE Customers are automatically upgraded to Premium when they meet the spending or order threshold. An email notification is sent upon upgrade. Tier status is evaluated on a rolling 12-month basis.  TIER DOWNGRADE If a customer falls below the Premium threshold for 12 consecutive months, they will be moved back to Standard tier with 30 days notice.
```

### Passage 2 (Relevance Score: `0.6630`)
- **Source S3 URI:** `s3://udacity-agentcore-policy-docs-237657481511-d7be52e0/policies/returns/return_policy.txt`
- **Content:**
```text
NovaMart Return Policy ======================= Last Updated: January 2025  STANDARD RETURN WINDOW Customers may return most items within 30 days of delivery for a full refund. Premium tier customers receive an extended 60-day return window.  ELIGIBLE ITEMS - Electronics: Must be in original packaging with all accessories included. - Clothing and Footwear: Must be unworn, unwashed, with original tags attached. - Appliances: Must be unused and in original packaging. - Books and Media: Eligible for return only if defective.  INELIGIBLE ITEMS - Perishable goods (food, flowers, plants) - Personalized or custom-made items - Digital downloads and software licenses - Items marked as "Final Sale" - Hazardous materials  RETURN PROCESS 1. Log in to your account and navigate to Order History. 2. Select the item you wish to return and click "Start Return." 3. Choose your reason for return from the dropdown menu. 4. Print the prepaid return shipping label. 5. Pack the item securely and drop it off at any authorized carrier location. 6. Refunds are processed within 5-7 business days of receiving the return.
```

### Passage 3 (Relevance Score: `0.6149`)
- **Source S3 URI:** `s3://udacity-agentcore-policy-docs-237657481511-d7be52e0/policies/returns/return_policy.txt`
- **Content:**
```text
Pack the item securely and drop it off at any authorized carrier location. 6. Refunds are processed within 5-7 business days of receiving the return.  REFUND METHODS - Original payment method (credit/debit card): 5-7 business days - Store credit: Immediate upon return approval - Gift returns: Store credit only  DAMAGED OR DEFECTIVE ITEMS If you receive a damaged or defective item, contact customer support within 48 hours of delivery. We will arrange a free return and send a replacement at no additional cost.  EXCHANGES Direct exchanges are available for clothing and footwear. All other exchanges must be processed as a return followed by a new purchase.  CONTACT For return assistance: support@novamart.example.com | 1-800-NOVA-456
```

---

## Shipping Policy Knowledge Base (`KX4W0TT4JJ`)
- **Natural Language Query:** `What are the shipping options, delivery times, and costs?`
- **Retrieved Passages Count:** 2

### Passage 1 (Relevance Score: `0.6565`)
- **Source S3 URI:** `s3://udacity-agentcore-policy-docs-237657481511-d7be52e0/policies/shipping/shipping_policy.txt`
- **Content:**
```text
NovaMart Shipping Policy ========================= Last Updated: January 2025  DOMESTIC SHIPPING OPTIONS Standard Shipping (5-7 business days): Free on orders over $50, $4.99 otherwise Expedited Shipping (2-3 business days): $9.99 Overnight Shipping (next business day): $24.99 Same-Day Delivery (select metros): $14.99  INTERNATIONAL SHIPPING We ship to over 50 countries. International shipping rates and delivery times vary by destination. Import duties and taxes are the responsibility of the recipient. Estimated delivery: 7-21 business days depending on destination.  ORDER PROCESSING Orders placed before 2:00 PM EST on business days are processed same day. Orders placed after 2:00 PM EST or on weekends are processed the next business day. Orders are not processed on federal holidays.  TRACKING A tracking number is emailed within 24 hours of shipment. Track your order at novamart.example.com/track or via the carrier's website.  DELIVERY ISSUES Lost packages: File a claim within 30 days of expected delivery date. Wrong address: Contact support immediately. Address changes after dispatch may incur fees. Missed delivery: The carrier will attempt delivery up to 3 times before holding at facility.  PREMIUM MEMBER BENEFITS Premium tier customers receive free expedited shipping on all orders.
```

### Passage 2 (Relevance Score: `0.5704`)
- **Source S3 URI:** `s3://udacity-agentcore-policy-docs-237657481511-d7be52e0/policies/shipping/customer_tiers.txt`
- **Content:**
```text
NovaMart Customer Tier Program ================================ Last Updated: January 2025  TIER OVERVIEW NovaMart offers two customer tiers: Standard and Premium.  STANDARD TIER - Default tier for all new customers - 30-day return window - Standard shipping rates apply - 1-year warranty on electronics - Standard customer support response time: 24-48 hours  PREMIUM TIER Requirements: Spend $500+ in a calendar year OR place 20+ orders in a calendar year. Benefits: - Extended 60-day return window - Free expedited shipping on all orders - 3-year warranty on electronics - Priority customer support: response within 4 hours - Early access to sales and new product launches - Dedicated account manager for orders over $500  HOW TO UPGRADE Customers are automatically upgraded to Premium when they meet the spending or order threshold. An email notification is sent upon upgrade. Tier status is evaluated on a rolling 12-month basis.  TIER DOWNGRADE If a customer falls below the Premium threshold for 12 consecutive months, they will be moved back to Standard tier with 30 days notice.
```

---

## Warranty Policy Knowledge Base (`BNUVVUDQ5J`)
- **Natural Language Query:** `What does the 1-year limited warranty cover and what is excluded?`
- **Retrieved Passages Count:** 2

### Passage 1 (Relevance Score: `0.6420`)
- **Source S3 URI:** `s3://udacity-agentcore-policy-docs-237657481511-d7be52e0/policies/warranty/warranty_policy.txt`
- **Content:**
```text
NovaMart Warranty Policy ========================== Last Updated: January 2025  STANDARD WARRANTY All NovaMart products come with a 1-year limited warranty against manufacturing defects. Electronics carry a 2-year warranty.   WARRANTY COVERAGE The warranty covers: - Manufacturing defects - Hardware failures under normal use - Defective materials  The warranty does NOT cover: - Damage from accidents, misuse, or negligence - Normal wear and tear - Water damage (unless product is rated waterproof) - Unauthorized modifications or repairs - Cosmetic damage (scratches, dents)  WARRANTY CLAIMS To file a warranty claim: 1. Contact support with proof of purchase and description of the defect. 2. Our team will assess the claim within 2 business days. 3. If approved, we will repair, replace, or refund at our discretion.  EXTENDED WARRANTY NovaMart Protection Plans are available for 2 or 3 years of additional coverage. Plans cover accidental damage in addition to manufacturing defects. Purchase within 30 days of product purchase for eligibility.  PREMIUM CUSTOMER WARRANTY Premium tier customers receive an automatic 3-year warranty on all Electronics.
```

### Passage 2 (Relevance Score: `0.5438`)
- **Source S3 URI:** `s3://udacity-agentcore-policy-docs-237657481511-d7be52e0/policies/warranty/customer_tiers.txt`
- **Content:**
```text
NovaMart Customer Tier Program ================================ Last Updated: January 2025  TIER OVERVIEW NovaMart offers two customer tiers: Standard and Premium.  STANDARD TIER - Default tier for all new customers - 30-day return window - Standard shipping rates apply - 1-year warranty on electronics - Standard customer support response time: 24-48 hours  PREMIUM TIER Requirements: Spend $500+ in a calendar year OR place 20+ orders in a calendar year. Benefits: - Extended 60-day return window - Free expedited shipping on all orders - 3-year warranty on electronics - Priority customer support: response within 4 hours - Early access to sales and new product launches - Dedicated account manager for orders over $500  HOW TO UPGRADE Customers are automatically upgraded to Premium when they meet the spending or order threshold. An email notification is sent upon upgrade. Tier status is evaluated on a rolling 12-month basis.  TIER DOWNGRADE If a customer falls below the Premium threshold for 12 consecutive months, they will be moved back to Standard tier with 30 days notice.
```

---
