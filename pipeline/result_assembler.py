from services.report_builder import build_report

def assemble_final_result(scores, weights, bias):
    return build_report(scores, weights, bias)
