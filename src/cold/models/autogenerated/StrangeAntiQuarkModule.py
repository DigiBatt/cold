
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SecondGenerationFermionModule import SecondGenerationFermion



from .DownAntiQuarkTypeModule import DownAntiQuarkType







class StrangeAntiQuark(SecondGenerationFermion, DownAntiQuarkType):
    """
    Class representing the `StrangeAntiQuark` entity, which inherits from:
    - SecondGenerationFermion, DownAntiQuarkType

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_f33cbdf9_c9d0_4dc5_a875_21d6f9c24ee4'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'StrangeAntiQuark'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = StrangeAntiQuark(
    
    class_iri='https://w3id.org/emmo#EMMO_f33cbdf9_c9d0_4dc5_a875_21d6f9c24ee4',
    
    class_name='StrangeAntiQuark',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_f33cbdf9_c9d0_4dc5_a875_21d6f9c24ee4',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'StrangeAntiQuark',
        alias="class_name"
    )
    

    
    

    

    