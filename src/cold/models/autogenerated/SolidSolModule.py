
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SolModule import Sol



from .SolidMixtureModule import SolidMixture



from .SolidModule import Solid







class SolidSol(Sol, SolidMixture, Solid):
    """
    Class representing the `SolidSol` entity, which inherits from:
    - Sol, SolidMixture, Solid

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_5add9885_dc98_4fa5_8482_fdf9ba5e3889'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'SolidSol'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = SolidSol(
    
    class_iri='https://w3id.org/emmo#EMMO_5add9885_dc98_4fa5_8482_fdf9ba5e3889',
    
    class_name='SolidSol',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_5add9885_dc98_4fa5_8482_fdf9ba5e3889',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'SolidSol',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    