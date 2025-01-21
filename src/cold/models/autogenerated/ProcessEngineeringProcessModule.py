
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .TechnologyProcessModule import TechnologyProcess







class ProcessEngineeringProcess(TechnologyProcess):
    """
    Class representing the `ProcessEngineeringProcess` entity, which inherits from:
    - TechnologyProcess

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_592b1d98_4736_4cac_9b62_849b8dbe11c7'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ProcessEngineeringProcess'`
        - **Alias**: `class_name`
    
    - `comment` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `comment`
    
    - `wikipediaReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikipediaReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ProcessEngineeringProcess(
    
    class_iri='https://w3id.org/emmo#EMMO_592b1d98_4736_4cac_9b62_849b8dbe11c7',
    
    class_name='ProcessEngineeringProcess',
    
    comment="example_value",
    
    wikipediaReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_592b1d98_4736_4cac_9b62_849b8dbe11c7',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ProcessEngineeringProcess',
        alias="class_name"
    )
    
    comment: Optional[str] = Field(
        None,
        alias="comment"
    )
    
    wikipediaReference: Optional[str] = Field(
        None,
        alias="wikipediaReference"
    )
    

    
    

    

    