
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .StrangeQuarkModule import StrangeQuark



from .GreenQuarkModule import GreenQuark







class GreenStrangeQuark(StrangeQuark, GreenQuark):
    """
    Class representing the `GreenStrangeQuark` entity, which inherits from:
    - StrangeQuark, GreenQuark

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_470697b1_a5bd_44b9_b00d_a77c9bcfb066'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'GreenStrangeQuark'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = GreenStrangeQuark(
    
    class_iri='https://w3id.org/emmo#EMMO_470697b1_a5bd_44b9_b00d_a77c9bcfb066',
    
    class_name='GreenStrangeQuark',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_470697b1_a5bd_44b9_b00d_a77c9bcfb066',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'GreenStrangeQuark',
        alias="class_name"
    )
    

    
    

    

    