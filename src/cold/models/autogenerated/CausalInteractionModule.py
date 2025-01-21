
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .FundamentalInteractionModule import FundamentalInteraction







class CausalInteraction(FundamentalInteraction):
    """
    Class representing the `CausalInteraction` entity, which inherits from:
    - FundamentalInteraction

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_50afa1a9_2c4e_40fd_aa93_0e33511f1f27'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'CausalInteraction'`
        - **Alias**: `class_name`
    
    - `conceptualisation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `conceptualisation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = CausalInteraction(
    
    class_iri='https://w3id.org/emmo#EMMO_50afa1a9_2c4e_40fd_aa93_0e33511f1f27',
    
    class_name='CausalInteraction',
    
    conceptualisation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_50afa1a9_2c4e_40fd_aa93_0e33511f1f27',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'CausalInteraction',
        alias="class_name"
    )
    
    conceptualisation: Optional[str] = Field(
        None,
        alias="conceptualisation"
    )
    

    
    

    

    