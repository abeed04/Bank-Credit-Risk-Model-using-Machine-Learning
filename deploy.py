

from flask import Flask,render_template,request
import pickle



app = Flask(__name__)


#load the model
model = pickle.load (open ('model.pkl' , 'rb'))



#home page
@app.route('/')
def home():
    return render_template('index.html', **locals())


@app.route('/predict', methods = ['POST','GET'])
def predict ():
    v1 = float(request.form['PROSPECTID'])
    v2 = float(request.form['Total_TL'])
    v3 = float(request.form['Tot_Closed_TL'])
    v4 = float(request.form['Tot_Active_TL'])
    v5 = float(request.form['Total_TL_opened_L6M'])
    v6 = float(request.form['Tot_TL_closed_L6M'])
    v7 = float(request.form['pct_tl_open_L6M'])
    v8 = float(request.form['pct_tl_closed_L6M'])
    v9 = float(request.form['pct_active_tl'])
    v10 = float(request.form['pct_closed_tl'])
    v11 = float(request.form['Total_TL_opened_L12M'])
    v12 = float(request.form['Tot_TL_closed_L12M'])
    v13 = float(request.form['pct_tl_open_L12M'])
    v14 = float(request.form['pct_tl_closed_L12M'])
    v15 = float(request.form['Tot_Missed_Pmnt'])
    v16 = float(request.form['Auto_TL'])
    v17 = float(request.form['CC_TL'])
    v18 = float(request.form['Consumer_TL'])
    v19 = float(request.form['Gold_TL'])
    v20 = float(request.form['Home_TL'])
    v21 = float(request.form['PL_TL'])
    v22 = float(request.form['Secured_TL'])
    v23 = float(request.form['Unsecured_TL'])
    v24 = float(request.form['Other_TL'])
    v25 = float(request.form['Age_Oldest_TL'])
    v26 = float(request.form['Age_Newest_TL'])
    v27 = float(request.form['time_since_recent_payment'])
    v28 = float(request.form['num_times_delinquent'])
    v29 = float(request.form['max_recent_level_of_deliq'])
    v30 = float(request.form['num_deliq_6mts'])
    v31 = float(request.form['num_deliq_12mts'])
    v32 = float(request.form['num_deliq_6_12mts'])
    v33 = float(request.form['num_times_30p_dpd'])
    v34 = float(request.form['num_times_60p_dpd'])
    v35 = float(request.form['num_std'])
    v36 = float(request.form['num_std_6mts'])
    v37 = float(request.form['num_std_12mts'])
    v38 = float(request.form['num_sub'])
    v39 = float(request.form['num_sub_6mts'])
    v40 = float(request.form['num_sub_12mts'])
    v41 = float(request.form['num_dbt'])
    v42 = float(request.form['num_dbt_6mts'])
    v43 = float(request.form['num_dbt_12mts'])
    v44 = float(request.form['num_lss'])
    v45 = float(request.form['num_lss_6mts'])
    v46 = float(request.form['num_lss_12mts'])
    v47 = float(request.form['recent_level_of_deliq'])
    v48 = float(request.form['tot_enq'])
    v49 = float(request.form['CC_enq'])
    v50 = float(request.form['CC_enq_L6m'])
    v51 = float(request.form['CC_enq_L12m'])
    v52 = float(request.form['PL_enq'])
    v53 = float(request.form['PL_enq_L6m'])
    v54 = float(request.form['PL_enq_L12m'])
    v55 = float(request.form['time_since_recent_enq'])
    v56 = float(request.form['enq_L12m'])
    v57 = float(request.form['enq_L6m'])
    v58 = float(request.form['enq_L3m'])
    v59 = float(request.form['EDUCATION'])
    v60 = float(request.form['AGE'])
    v61 = float(request.form['NETMONTHLYINCOME'])
    v62 = float(request.form['Time_With_Curr_Empr'])
    v63 = float(request.form['pct_of_active_TLs_ever'])
    v64 = float(request.form['pct_opened_TLs_L6m_of_L12m'])
    v65 = float(request.form['pct_currentBal_all_TL'])
    v66 = float(request.form['CC_Flag'])
    v67 = float(request.form['PL_Flag'])
    v68 = float(request.form['pct_PL_enq_L6m_of_L12m'])
    v69 = float(request.form['pct_CC_enq_L6m_of_L12m'])
    v70 = float(request.form['pct_PL_enq_L6m_of_ever'])
    v71 = float(request.form['pct_CC_enq_L6m_of_ever'])
    v72 = float(request.form['HL_Flag'])
    v73 = float(request.form['GL_Flag'])
    v74 = float(request.form['Credit_Score'])
    v75 = float(request.form['MARITALSTATUS_Married'])
    v76 = float(request.form['MARITALSTATUS_Single'])
    v77 = float(request.form['GENDER_F'])
    v78 = float(request.form['GENDER_M'])
    v79 = float(request.form['last_prod_enq2_AL'])
    v80 = float(request.form['last_prod_enq2_CC'])
    v81 = float(request.form['last_prod_enq2_ConsumerLoan'])
    v82 = float(request.form['last_prod_enq2_HL'])
    v83 = float(request.form['last_prod_enq2_PL'])
    v84 = float(request.form['last_prod_enq2_others'])
    v85 = float(request.form['first_prod_enq2_AL'])
    v86 = float(request.form['first_prod_enq2_CC'])
    v87 = float(request.form['first_prod_enq2_ConsumerLoan'])
    v88 = float(request.form['first_prod_enq2_HL'])
    v89 = float(request.form['first_prod_enq2_PL'])
    v90 = float(request.form['first_prod_enq2_others'])

    result = model.predict ([[v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, v15, v16, v17, v18, v19, v20,
                v21, v22, v23, v24, v25, v26, v27, v28, v29, v30, v31, v32, v33, v34, v35, v36, v37, v38, v39,
                v40, v41, v42, v43, v44, v45, v46, v47, v48, v49, v50, v51, v52, v53, v54, v55, v56, v57, v58,
                v59, v60, v61, v62, v63, v64, v65, v66, v67, v68, v69, v70, v71, v72, v73, v74, v75, v76, v77,
                v78, v79, v80, v81, v82, v83, v84, v85, v86, v87, v88, v89, v90]]) [0]

    return render_template('index.html', **locals())



if __name__ == '__main__':
    app.run ()








