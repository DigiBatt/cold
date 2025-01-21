
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SubstanceModule import Substance







class MesoscopicSubstance(Substance):
    """
    Class representing the `MesoscopicSubstance` entity, which inherits from:
    - Substance

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_660a4964_0333_4663_bc66_e93ef59b0679'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'MesoscopicSubstance'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = MesoscopicSubstance(
    
    class_iri='https://w3id.org/emmo#EMMO_660a4964_0333_4663_bc66_e93ef59b0679',
    
    class_name='MesoscopicSubstance',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_660a4964_0333_4663_bc66_e93ef59b0679',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'MesoscopicSubstance',
        alias="class_name"
    )
    

    
    

    

    