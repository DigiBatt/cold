
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SuspensionModule import Suspension



from .SolidMixtureModule import SolidMixture



from .SolidModule import Solid







class SolidGasSuspension(Suspension, SolidMixture, Solid):
    """
    Class representing the `SolidGasSuspension` entity, which inherits from:
    - Suspension, SolidMixture, Solid

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_c457b6b9_5e73_4853_ae08_d776c12b8058'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'SolidGasSuspension'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = SolidGasSuspension(
    
    class_iri='https://w3id.org/emmo#EMMO_c457b6b9_5e73_4853_ae08_d776c12b8058',
    
    class_name='SolidGasSuspension',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_c457b6b9_5e73_4853_ae08_d776c12b8058',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'SolidGasSuspension',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    