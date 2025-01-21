
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .DispersionModule import Dispersion



from .PhaseHomogeneousMixtureModule import PhaseHomogeneousMixture







class Solution(Dispersion, PhaseHomogeneousMixture):
    """
    Class representing the `Solution` entity, which inherits from:
    - Dispersion, PhaseHomogeneousMixture

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_2031516a_2be7_48e8_9af7_7e1270e308fe'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Solution'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Solution(
    
    class_iri='https://w3id.org/emmo#EMMO_2031516a_2be7_48e8_9af7_7e1270e308fe',
    
    class_name='Solution',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_2031516a_2be7_48e8_9af7_7e1270e308fe',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Solution',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    