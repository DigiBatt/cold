
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ElectricResistanceModule import ElectricResistance



from .SIExactConstantModule import SIExactConstant







class VonKlitzingConstant(ElectricResistance, SIExactConstant):
    """
    Class representing the `VonKlitzingConstant` entity, which inherits from:
    - ElectricResistance, SIExactConstant

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_eb561764_276e_413d_a8cb_3a3154fd9bf8'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'VonKlitzingConstant'`
        - **Alias**: `class_name`
    
    - `definition` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `definition`
    
    - `qudtReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `qudtReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = VonKlitzingConstant(
    
    class_iri='https://w3id.org/emmo#EMMO_eb561764_276e_413d_a8cb_3a3154fd9bf8',
    
    class_name='VonKlitzingConstant',
    
    definition="example_value",
    
    qudtReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_eb561764_276e_413d_a8cb_3a3154fd9bf8',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'VonKlitzingConstant',
        alias="class_name"
    )
    
    definition: Optional[str] = Field(
        None,
        alias="definition"
    )
    
    qudtReference: Optional[str] = Field(
        None,
        alias="qudtReference"
    )
    

    
    

    

    