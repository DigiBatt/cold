
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .GasMixtureModule import GasMixture



from .SuspensionModule import Suspension



from .GasModule import Gas







class GasSolidSuspension(GasMixture, Suspension, Gas):
    """
    Class representing the `GasSolidSuspension` entity, which inherits from:
    - GasMixture, Suspension, Gas

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_d4f37e32_16ae_4cc6_b4cd_fd896b2449c4'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'GasSolidSuspension'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `example` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `example`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = GasSolidSuspension(
    
    class_iri='https://w3id.org/emmo#EMMO_d4f37e32_16ae_4cc6_b4cd_fd896b2449c4',
    
    class_name='GasSolidSuspension',
    
    elucidation="example_value",
    
    example="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_d4f37e32_16ae_4cc6_b4cd_fd896b2449c4',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'GasSolidSuspension',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    example: Optional[str] = Field(
        None,
        alias="example"
    )
    

    
    

    

    