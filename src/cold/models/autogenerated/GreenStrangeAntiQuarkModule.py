
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .StrangeAntiQuarkModule import StrangeAntiQuark



from .GreenAntiQuarkModule import GreenAntiQuark







class GreenStrangeAntiQuark(StrangeAntiQuark, GreenAntiQuark):
    """
    Class representing the `GreenStrangeAntiQuark` entity, which inherits from:
    - StrangeAntiQuark, GreenAntiQuark

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_ab922466_6333_4f13_91e6_03c3cad13ed8'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'GreenStrangeAntiQuark'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = GreenStrangeAntiQuark(
    
    class_iri='https://w3id.org/emmo#EMMO_ab922466_6333_4f13_91e6_03c3cad13ed8',
    
    class_name='GreenStrangeAntiQuark',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_ab922466_6333_4f13_91e6_03c3cad13ed8',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'GreenStrangeAntiQuark',
        alias="class_name"
    )
    

    
    

    

    