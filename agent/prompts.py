def generate_agent_role_prompt(agent):
    """ Generates the agent role prompt.
    Args: agent (str): The type of the agent.
    Returns: str: The agent role prompt.
    """
    prompts = {
        "Default Agent": "You are an AI critical thinker research assistant. Your sole purpose is to write well written, critically acclaimed, objective and structured reports on given text.",
        "Customer Listener Agent": "You are an experienced marketer. Your purpose is to compile research on what people are saying about a product or niche and learn to leverage their language for direct response copy."
    }

    return prompts.get(agent, "No such agent")


def generate_search_queries_prompt(question):
    """ Generates the search queries prompt for the given question.
    Args: question (str): The question to generate the search queries prompt for
    Returns: str: The search queries prompt for the given question
    """

    return f'Write 4 google search queries to search on reddit and forums that form an objective opinion from the following: "{question}"'\
           f'You must respond with a list of strings in the following format: ["query 1", "query 2", "query 3", "query 4"]'


def generate_customer_language_report_prompt(question, research_summary):
    """ Generates the customer language report prompt for the given question and research summary.
    Args: question (str): The question to generate the customer language report prompt for
            research_summary (str): The research summary to generate the customer language report prompt for
    Returns: str: The customer language report prompt for the given question and research summary
    """

    return f'"""{research_summary}""" Using the above information, answer the following'\
           f' question or topic: "{question}" in a detailed report to be used in Facebook ad copy --'\
           " The report should focus on the answer to the question, should be well structured, informative," \
           " in depth, with personal quotes, reviews, and stories if available, a minimum of 1,200 words and with markdown syntax and apa format. "\
            "Use the language you find to list pain points, day to day problems, what solutions they tried but failed"\
            "The report should help marketers leverage what people are saying online to create compelling Facebook ad copy" \
            "Do NOT deter to general and meaningless conclusions." \
           "Write all source urls at the end of the report in apa format"


def generate_scripts_prompt(question, research_summary):
    """ Generates the customer language report prompt for the given question and research summary.
    Args: question (str): The question to generate the customer language report prompt for
            research_summary (str): The research summary to generate the customer language report prompt for
    Returns: str: The customer language report prompt for the given question and research summary
    """

    return f'"""{research_summary}""" Using the above information, write 3 Facebook video ad scripts for me with the constraints below.'\
        'You are an expert copywriter tasked with writing effective scripts for Facebook video ads that will compel users to purchase.'\
        'If you can, you must satisfy all the constraints listed below. If you are unable to do it, you still have to satisfy as much as you can.'\
        'Constraint 1: Don’t be salesy and clickbaity. The style of the copy should be natural, when reading out loud it should sound like a real person who is not trying to sell anything.'\
        'Constraint 2: Don’t use jargon, use plain english that is easy to understand.'\
        'Constraint 3: Use the organic language and stories from the above information as much as it makes sense. Ad copy using the customer wording resonates better in copy'\
        'Constraint 4: Set up the script in a Markdown syntax and divide it into the following sections: Hook, Problem Intro, Problem Agitation, Failed Solution, Product Intro, Features/USPs, Benefits, Desired End Result, Call to action'\
        'Constraint 5: The product is a new online back pain coaching service.'\
        'Constraint 6: The scripts should be concise and shorter than 30 seconds to read through.'\
        'Constraint 7: Write me 3 scripts.'\
        'Constraint 8: Write all source URLs at the end of the report in APA format.'\
        f'Constraint 9: Finally, write a keyword related to "{question}" to search the stock video site Pexels for relevant clips to create a video ad. Your output should only include the keywords with maximum of 3 words for one search. No commas. It should follow this format: KEYWORDS: (your keywords here)'
           
def generate_keywords_prompt(research_summary):
    """ Generates the keyword prompt for the given question and research summary.
    Args: question (str): The question to generate the keyword prompt for
            research_summary (str): The research summary to generate the keyword prompt for
    Returns: str: The keyword prompt for the given question and research summary
    """

    return f'"""{research_summary}""" Using the above information, write a keyword to search a stock video site for relevant clips to create a video ad.'\
        'Your output should only include the keywords with maximum 5 words for one search. Not any other words.'\


def generate_hook_prompt():



    return "dynamic video title"


def get_report_by_type(report_type):
    report_type_mapping = {
        'customer_language_report': generate_customer_language_report_prompt,
        'script_writer_report': generate_scripts_prompt
        #'create_video_ads': new_function_tbd
    }
    return report_type_mapping[report_type]