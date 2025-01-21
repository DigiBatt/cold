
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .GasMixtureModule import GasMixture



from .SolutionModule import Solution







class GasSolution(GasMixture, Solution):
    """
    Class representing the `GasSolution` entity, which inherits from:
    - GasMixture, Solution

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_5be9c137_325a_43d8_b7cd_ea93e7721c2d'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'GasSolution'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = GasSolution(
    
    class_iri='https://w3id.org/emmo#EMMO_5be9c137_325a_43d8_b7cd_ea93e7721c2d',
    
    class_name='GasSolution',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_5be9c137_325a_43d8_b7cd_ea93e7721c2d',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'GasSolution',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    