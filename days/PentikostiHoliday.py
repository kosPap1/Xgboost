def pentikosti():

    # Prediction for Pentikosti Holiday

    # Libraries imports
    from functions.dataInput import load2013, load2014, load2015, load2016, load2017, load2018, load2019, load2013, temp2013, temp2014, \
        temp2015, temp2016, temp2017, temp2018, temp2019
    from functions.predictionEngine import predictionEngine1, predictionEngineCase2, predictionEngineCase3,\
        predictionEngineCase4
    import os

    # Holiday Datasets Lags

    # 13. Pentikosti Holiday

    # Train Load lag inputs
    loadTrainDayTarget = load2015['2015-05-31']
    loadTrainDayMinus1 = load2015['2015-05-30']
    loadTrainDayMinus7 = load2015['2015-05-24']
    loadTrainDayMinus365 = load2014['2014-06-08']
    loadTrainDayMinus730 = load2013['2013-06-23']

    # Train temperature lag inputs
    temperTrainDayTarget = temp2015['2015-05-31']
    temperTrainDayMinus1 = temp2015['2015-05-30']
    temperTrainDayMinus7 = temp2015['2015-05-24']
    temperTrainDayMinus365 = temp2014['2014-06-08']
    temperTrainDayMinus730 = temp2013['2013-06-23']

    ##############################################
    # Test lag days input

    loadTestDayTarget = load2019['2019-06-16']
    loadTestDayMinus1 = load2019['2019-06-15']
    loadTestDayMinus7 = load2019['2019-06-09']
    loadTestDayMinus365 = load2018['2018-05-27']
    loadTestDayMinus730 = load2017['2017-06-04']

    # Train temperature lag inputs
    temperTestDayTarget = temp2019['2019-06-16']
    temperTestDayMinus1 = temp2019['2019-06-15']
    temperTestDayMinus7 = temp2019['2019-06-09']
    temperTestDayMinus365 = temp2018['2018-05-27']
    temperTestDayMinus730 = temp2017['2017-06-04']

    ########################################################################################################################
    filename = os.path.basename(__file__)

    # predictionEngine1(loadTrainDayTarget, loadTrainDayMinus1, loadTrainDayMinus7, loadTrainDayMinus365,
    #                  loadTestDayTarget, loadTestDayMinus1, loadTestDayMinus7, loadTestDayMinus365, filename)

    # # Case 2
    # predictionEngineCase2(loadTrainDayTarget, loadTrainDayMinus1, loadTrainDayMinus7, loadTrainDayMinus365,
    #                       loadTestDayTarget, loadTestDayMinus1, loadTestDayMinus7, loadTestDayMinus365, filename)

    # Case 3
    predictionEngineCase3(loadTrainDayTarget, loadTrainDayMinus1, loadTrainDayMinus7, loadTrainDayMinus365,
                          loadTestDayTarget, loadTestDayMinus1, loadTestDayMinus7, loadTestDayMinus365,
                          temperTrainDayTarget, temperTrainDayMinus1, temperTrainDayMinus7, temperTrainDayMinus365,
                          temperTestDayTarget, temperTestDayMinus1, temperTestDayMinus7, temperTestDayMinus365,
                          filename)

    # Case 4

    # predictionEngineCase4(loadTrainDayTarget, loadTrainDayMinus1, loadTrainDayMinus7, loadTrainDayMinus365,
    #                       loadTestDayTarget, loadTestDayMinus1, loadTestDayMinus7, loadTestDayMinus365,
    #                       temperTrainDayTarget, temperTrainDayMinus1, temperTrainDayMinus7, temperTrainDayMinus365,
    #                       temperTestDayTarget, temperTestDayMinus1, temperTestDayMinus7, temperTestDayMinus365,
    #                       filename)