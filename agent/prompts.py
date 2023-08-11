def generate_agent_role_prompt(agent):
    """ Generates the agent role prompt.
    Args: agent (str): The type of the agent.
    Returns: str: The agent role prompt.
    """
    prompts = {
        "Finance Agent": "You are a seasoned finance analyst AI assistant. Your primary goal is to compose comprehensive, astute, impartial, and methodically arranged financial reports based on provided data and trends.",
        "Travel Agent": "You are a world-travelled AI tour guide assistant. Your main purpose is to draft engaging, insightful, unbiased, and well-structured travel reports on given locations, including history, attractions, and cultural insights.",
        "Academic Research Agent": "You are an AI academic research assistant. Your primary responsibility is to create thorough, academically rigorous, unbiased, and systematically organized reports on a given research topic, following the standards of scholarly work.",
        "Business Analyst": "You are an experienced AI business analyst assistant. Your main objective is to produce comprehensive, insightful, impartial, and systematically structured business reports based on provided business data, market trends, and strategic analysis.",
        "Computer Security Analyst Agent": "You are an AI specializing in computer security analysis. Your principal duty is to generate comprehensive, meticulously detailed, impartial, and systematically structured reports on computer security topics. This includes Exploits, Techniques, Threat Actors, and Advanced Persistent Threat (APT) Groups. All produced reports should adhere to the highest standards of scholarly work and provide in-depth insights into the complexities of computer security.",
        "Default Agent": "You are an AI critical thinker research assistant. Your sole purpose is to write well written, critically acclaimed, objective and structured reports on given text.",
        "Customer Listener Agent": "You are an experienced marketer. Your purpose is to compile research on what people are saying about a product or niche and learn to leverage their language for direct response copy."
    }

    return prompts.get(agent, "No such agent")


def generate_report_prompt(question, research_summary):
    """ Generates the report prompt for the given question and research summary.
    Args: question (str): The question to generate the report prompt for
            research_summary (str): The research summary to generate the report prompt for
    Returns: str: The report prompt for the given question and research summary
    """

    return f'"""{research_summary}""" Using the above information, answer the following'\
           f' question or topic: "{question}" in a detailed report --'\
           " The report should focus on the answer to the question, should be well structured, informative," \
           " in depth, with facts and numbers if available, a minimum of 1,200 words and with markdown syntax and apa format. "\
            "You MUST determine your own concrete and valid opinion based on the information found. Do NOT deter to general and meaningless conclusions." \
           "Write all source urls at the end of the report in apa format"

def generate_search_queries_prompt(question):
    """ Generates the search queries prompt for the given question.
    Args: question (str): The question to generate the search queries prompt for
    Returns: str: The search queries prompt for the given question
    """

    return f'Write 4 google search queries to search on reddit and forums that form an objective opinion from the following: "{question}"'\
           f'You must respond with a list of strings in the following format: ["query 1", "query 2", "query 3", "query 4"]'


def generate_resource_report_prompt(question, research_summary):
    """Generates the resource report prompt for the given question and research summary.

    Args:
        question (str): The question to generate the resource report prompt for.
        research_summary (str): The research summary to generate the resource report prompt for.

    Returns:
        str: The resource report prompt for the given question and research summary.
    """
    return f'"""{research_summary}""" Based on the above information, generate a bibliography recommendation report for the following' \
           f' question or topic: "{question}". The report should provide a detailed analysis of each recommended resource,' \
           ' explaining how each source can contribute to finding answers to the research question.' \
           ' Focus on the relevance, reliability, and significance of each source.' \
           ' Ensure that the report is well-structured, informative, in-depth, and follows Markdown syntax.' \
           ' Include relevant facts, figures, and numbers whenever available.' \
           ' The report should have a minimum length of 1,200 words.'


def generate_outline_report_prompt(question, research_summary):
    """ Generates the outline report prompt for the given question and research summary.
    Args: question (str): The question to generate the outline report prompt for
            research_summary (str): The research summary to generate the outline report prompt for
    Returns: str: The outline report prompt for the given question and research summary
    """

    return f'"""{research_summary}""" Using the above information, generate an outline for a research report in Markdown syntax'\
           f' for the following question or topic: "{question}". The outline should provide a well-structured framework'\
           ' for the research report, including the main sections, subsections, and key points to be covered.' \
           ' The research report should be detailed, informative, in-depth, and a minimum of 1,200 words.' \
           ' Use appropriate Markdown syntax to format the outline and ensure readability.'


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
        'Constraint 4: Set up the script in a Markdown syntax and divide it into the following sections: Hook, Problem Intro, Problem Agitation, Failed Solution, Product Intro, Features/USPs, Benefits, Desired End Result, Social Proof/Testimonial, Call to action'\
        'Constraint 5: The product is a new online back pain coaching service.'\
        'Constraint 6: The scripts should be concise and shorter than 30 seconds to read through.'\
        'Constraint 7: Write me 3 scripts.'\
        'Constraint 8: Write all source URLs at the end of the report in APA format.'\
           


def generate_concepts_prompt(question, research_summary):
    """ Generates the concepts prompt for the given question.
    Args: question (str): The question to generate the concepts prompt for
            research_summary (str): The research summary to generate the concepts prompt for
    Returns: str: The concepts prompt for the given question
    """

    return f'"""{research_summary}""" Using the above information, generate a list of 5 main concepts to learn for a research report'\
           f' on the following question or topic: "{question}". The outline should provide a well-structured framework'\
           'You must respond with a list of strings in the following format: ["concepts 1", "concepts 2", "concepts 3", "concepts 4, concepts 5"]'


def generate_lesson_prompt(concept):
    """
    Generates the lesson prompt for the given question.
    Args:
        concept (str): The concept to generate the lesson prompt for.
    Returns:
        str: The lesson prompt for the given concept.
    """

    prompt = f'generate a comprehensive lesson about {concept} in Markdown syntax. This should include the definition'\
    f'of {concept}, its historical background and development, its applications or uses in different'\
    f'fields, and notable events or facts related to {concept}.'

    return prompt

def get_report_by_type(report_type):
    report_type_mapping = {
       # 'research_report': generate_report_prompt,
       # 'resource_report': generate_resource_report_prompt,
       # 'outline_report': generate_outline_report_prompt,
        'customer_language_report': generate_customer_language_report_prompt,
        'script_writer_report': generate_scripts_prompt
    }
    return report_type_mapping[report_type]