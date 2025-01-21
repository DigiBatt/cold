
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .GasMixtureModule import GasMixture



from .ColloidModule import Colloid



from .GasModule import Gas







class Aerosol(GasMixture, Colloid, Gas):
    """
    Class representing the `Aerosol` entity, which inherits from:
    - GasMixture, Colloid, Gas

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_560d833a_6184_410c_859a_05d982712fd7'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Aerosol'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Aerosol(
    
    class_iri='https://w3id.org/emmo#EMMO_560d833a_6184_410c_859a_05d982712fd7',
    
    class_name='Aerosol',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_560d833a_6184_410c_859a_05d982712fd7',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Aerosol',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    