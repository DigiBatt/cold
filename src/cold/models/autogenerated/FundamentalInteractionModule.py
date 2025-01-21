
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CausalSystemModule import CausalSystem







class FundamentalInteraction(CausalSystem):
    """
    Class representing the `FundamentalInteraction` entity, which inherits from:
    - CausalSystem

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_43a4e80d_6ae9_45ed_8cfb_fd0a5339bf87'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'FundamentalInteraction'`
        - **Alias**: `class_name`
    
    - `conceptualisation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `conceptualisation`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `comment` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `comment`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = FundamentalInteraction(
    
    class_iri='https://w3id.org/emmo#EMMO_43a4e80d_6ae9_45ed_8cfb_fd0a5339bf87',
    
    class_name='FundamentalInteraction',
    
    conceptualisation="example_value",
    
    elucidation="example_value",
    
    comment="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_43a4e80d_6ae9_45ed_8cfb_fd0a5339bf87',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'FundamentalInteraction',
        alias="class_name"
    )
    
    conceptualisation: Optional[str] = Field(
        None,
        alias="conceptualisation"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    comment: Optional[str] = Field(
        None,
        alias="comment"
    )
    

    
    

    

    